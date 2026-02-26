from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AssetViewSet,
    VulnerabilityViewSet,
    RiskAssessmentViewSet,
    DashboardView, HomeView,
)

router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'vulnerabilities', VulnerabilityViewSet)
router.register(r'risks', RiskAssessmentViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', include(router.urls)),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
