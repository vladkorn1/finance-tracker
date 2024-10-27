from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from transactions.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'goals', GoalViewSet, basename='goals')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transactions.urls')),
    path('api/v1/', include((router.urls, ''))),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/categories/', CategoryAPIList.as_view(), name='categories'),
    path('api/v1/categories/<int:pk>/', CategoryAPIUpdate.as_view()),
    path('api/v1/category_delete/<int:pk>/', CategoryAPIDestroy.as_view()),
    path('api/v1/', include((router.urls, ''))),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/registration/', signup, name='signup'),
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
