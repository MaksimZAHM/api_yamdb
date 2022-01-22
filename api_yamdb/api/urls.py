from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import sign_up, get_token, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token, name='token'),
    path('v1/auth/signup/', sign_up, name='signup')
]
