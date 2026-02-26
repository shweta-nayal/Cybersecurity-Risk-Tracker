from rest_framework import viewsets
from django.db.models import Count
from .models import Asset, Vulnerability, RiskAssessment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    AssetSerializer,
    VulnerabilitySerializer,
    RiskAssessmentSerializer
)


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class VulnerabilityViewSet(viewsets.ModelViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer


class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer

class DashboardView(APIView):
    def get(self, request):
        # Basic counts
        total_assets = Asset.objects.count()
        total_vulnerabilities = Vulnerability.objects.count()
        total_risks = RiskAssessment.objects.count()

        # Highest risk score
        highest_risk = RiskAssessment.objects.order_by('-risk_score').first()
        highest_risk_score = highest_risk.risk_score if highest_risk else 0

        # Critical vulnerabilities
        critical_vulns = Vulnerability.objects.filter(severity="CRITICAL").count()

        # Vulnerability severity distribution (for charts)
        severity_distribution = (
            Vulnerability.objects
            .values('severity')
            .annotate(count=Count('id'))
            .order_by('-count')
        )

        # Top 5 highest risk assets
        top_risk_assets = (
            RiskAssessment.objects
            .select_related('vulnerability__asset')
            .order_by('-risk_score')[:5]
        )

        top_assets_data = [
            {
                "asset_name": risk.vulnerability.asset.name,
                "risk_score": risk.risk_score
            }
            for risk in top_risk_assets
        ]

        data = {
            "summary": {
                "total_assets": total_assets,
                "total_vulnerabilities": total_vulnerabilities,
                "total_risk_assessments": total_risks,
                "highest_risk_score": highest_risk_score,
                "critical_vulnerabilities": critical_vulns,
            },
            "severity_distribution": list(severity_distribution),
            "top_risk_assets": top_assets_data,
        }

        return Response(data)