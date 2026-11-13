from django.db import models
import uuid

class FundoImobiliario(models.Model):
    SETOR_CHOICES = [
        ('hospital', 'Hospital'),
        ('hotel', 'Hotel'),
        ('hibrido', 'Hibrido'),
        ('lajes_corporativas', 'Lajes Corporativas'),
        ('logistica', 'Logística'),
        ('outros', 'Outros'),
        ('residencial', 'Residencial'),
        ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    codigo = models.CharField(
        max_length=8,
        null=False,
        blank=False,
    )

    setor = models.CharField(
        max_length=30,
        choices=SETOR_CHOICES,
        null=False,
        blank=False,
    )

    dividend_yield_medio_12m = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )

    vacancia_financeira = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    vacancia_fisica = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
    )

    quantidade_ativos = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.codigo} - {self.get_setor_display()}"