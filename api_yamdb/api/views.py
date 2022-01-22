from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework import viewsets, status, filters, pagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import SignUpSerializer, UserSerializer, TokenSerializer
from .permissions import isAdminPermission

User = get_user_model()


@api_view(['POST'])
@permission_classes((AllowAny,))
def get_token(request):
    username = request.data.get('username', None)
    confirmation_code = request.data.get('confirmation_code', None)
    serializer = TokenSerializer(
        data={
            'username': username,
            'confirmation_code': confirmation_code
        })
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, username=username)

    if not default_token_generator.check_token(
        user, confirmation_code
    ) and confirmation_code != user.confirmation_code:
        return Response(
            'Неверный код подтверждения',
            status=status.HTTP_400_BAD_REQUEST)

    token = RefreshToken.for_user(user)
    response = {
        'token': str(token.access_token)
    }
    return Response(response, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (isAdminPermission, )
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('username', )
    lookup_fileds = 'username'
    pagination_class = pagination.LimitOffsetPagination

    @action(methods=['GET', 'PATCH'],
            url_path='me',
            permission_classes=(IsAuthenticated, ),
            detail=False)
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status.HTTP_200_OK)

        if request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=request.user.role)
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    username = request.data.get('username')
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        user = get_object_or_404(User, username=username)
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject='Вы зарегистрировались на YAMDB!',
            message=confirmation_code,
            from_email=settings.EMAIL_FROM,
            recipient_list=(user.email,)
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
