from rest_framework import serializers
from .models import Asset, Vulnerability, RiskAssessment

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = '__all__'


class RiskAssessmentSerializer(serializers.ModelSerializer):
    risk_score = serializers.ReadOnlyField()

    class Meta:
        model = RiskAssessment
        fields = '__all__'

    def create(self, validated_data):
        likelihood = validated_data.get("likelihood")
        impact = validated_data.get("impact")

        # simple formula
        validated_data["risk_score"] = likelihood * impact

        return super().create(validated_data)