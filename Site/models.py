from django.db import models
import uuid
# Create your models here.
class Vaga(models.Models):
    id = models.UUIDField(default=uuid.uuid4, editable=False , primary_key=True, serialize=False)
    empresa = models.CharField(max_length= 150)
    cargo = models.CharField(max_length=80)
    requisito = models.TextField()
    salario = models.BigIntegerField()
    experiencia = models.TextField()
    carga_h = models.IntegerField()
    beneficios = models.TextField()
    cidade = models.CharField(max_length=80)
    regime = models.TextChoices()
    vagas = models.IntegerField()
    detalhes = models.TextField()
    disponivel = models.BooleanField()
    pcd = models.BooleanField()