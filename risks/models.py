from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="vulnerabilities"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)

    def __str__(self):
        return self.title


class RiskAssessment(models.Model):
    vulnerability = models.OneToOneField(
        Vulnerability,
        on_delete=models.CASCADE,
        related_name="risk_assessment"
    )
    likelihood = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1 to 5 scale"
    )
    impact = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1 to 5 scale"
    )
    risk_score = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.risk_score = self.likelihood * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Risk Score: {self.risk_score}"
