from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# ✅ Add this import
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import RegisterView, PostViewSet, HomeView, AboutView, LikePostView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/home/', HomeView.as_view(), name='home'),
    path('api/about/', AboutView.as_view(), name='about'),
    path('api/posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
