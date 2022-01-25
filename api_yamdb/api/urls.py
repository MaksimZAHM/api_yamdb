from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (sign_up, get_token, UserViewSet,
                       CommentViewSet, ReviewViewSet,
                       CategoryViewSet, GenreViewSet, TitleViewSet)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token, name='token'),
    path('v1/auth/signup/', sign_up, name='signup')
]
