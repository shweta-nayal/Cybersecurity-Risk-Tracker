from django.contrib import admin
from .models import Asset, Vulnerability, RiskAssessment


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")


@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "severity", "asset")


@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ("vulnerability", "likelihood", "impact", "risk_score")
    readonly_fields = ("risk_score",)
