from django.contrib import admin
from django.urls import path, include
from filmapp.views import *

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("aktyorlar", AktyorViewSet),
router.register("kinolar", KinoViewSet),
# router.register("commentlar", CommentViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
    # path('kinolar/', KinolarAPIView.as_view()),
    path('comments/', CommentsAPIView.as_view()),
    # path('aktyorlar/', AktyorlarAPIView.as_view()),
    # path('aktyor/<int:pk>/', AktyorAPIView.as_view()),
]