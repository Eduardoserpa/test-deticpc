from django.db import models

# Create your models here.
class Objeto_tipo(models.Model):
    id = models.PositiveSmallIntegerField #SMALLINT
    tipo_de_objeto = models.CharField(max_length=64) #VARCHAR(64)

class Calibre(models.Model):
    id = models.PositiveSmallIntegerField #SMALLINT
    desc_calibre = models.CharField(max_length=45) #VARCHAR(45)

class Objeto(models.Model):
    id = models.PositiveBigIntegerField #BIGINT
    objeto_tipo_id = models.ForeignKey("Objeto_tipo", on_delete=models.SET_NULL, null=True) #SMALLINT

class Arma(models.Model):
    id = models.PositiveBigIntegerField #BIGINT
    calibre_id = models.ForeignKey("Calibre", on_delete=models.SET_NULL, null=True) #SMALLINT
    marca = models.CharField(max_length=64) #VARCHAR(64)
    modelo = models.CharField(max_length=64) #VARCHAR(64)
    quantidade_de_tiros = models.PositiveIntegerField #INT
    valor_estimado = models.DecimalField(max_digits = 30, decimal_places=15) #DOUBLE
    imagem = models.CharField(max_length=128) #VARCHAR(128)

class Municao(models.Model):
    id = models.PositiveBigIntegerField #BIGINT
    calibre_id = models.ForeignKey("Calibre", on_delete=models.SET_NULL, null=True) #SMALLINT
    marca = models.CharField(max_length=64) #VARCHAR(64)
    modelo = models.CharField(max_length=64) #VARCHAR(64)
    valor_estimado = models.DecimalField(max_digits = 30, decimal_places=15) #DOUBLE
