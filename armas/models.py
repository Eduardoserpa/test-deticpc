from django.db import models

"""class ArmasManager(models.Manager):
    def criar_arma(self, id, calibre_id, marca, modelo, quantidade_de_tiros, valor_estimado, imagem):
        objeto_arma = self.create(id=id, calibre_id=calibre_id, marca=marca, modelo=modelo, quantidade_de_tiros=quantidade_de_tiros, valor_estimado=valor_estimado, imagem=imagem)
        objeto_arma.save()

        objeto_objeto = self.create()
        objeto_objeto.save()

    
    def criar_municao(self, id, calibre_id, marca, modelo, valor_estimado):
        objeto_municao = self.create(id=id, calibre_id=calibre_id, marca=marca, modelo=modelo, valor_estimado=valor_estimado)
        objeto_municao.save()

        objeto_objeto = self.create()
        objeto_objeto.save()"""

class Objeto_tipo(models.Model):
    id = models.PositiveSmallIntegerField #SMALLINT
    tipo_de_objeto = models.CharField(max_length=64) #VARCHAR(64)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Calibre(models.Model):
    id = models.PositiveSmallIntegerField #SMALLINT
    desc_calibre = models.CharField(max_length=45) #VARCHAR(45)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Objeto(models.Model):
    #objects = ArmasManager()
    #Para instanciar o objeto: objeto = Objeto.objects.criar_objeto

    id = models.PositiveBigIntegerField #BIGINT
    objeto_tipo_id = models.ForeignKey("Objeto_tipo", on_delete=models.SET_NULL, null=True) #SMALLINT

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Arma(models.Model):
    #objects = ArmasManager()
    #Para instanciar o objeto: arma = Arma.objects.criar_arma

    id = models.OneToOneField("Objeto", primary_key=True, on_delete=models.CASCADE) #BIGINT
    calibre_id = models.ForeignKey("Calibre", on_delete=models.SET_NULL, null=True) #SMALLINT
    marca = models.CharField(max_length=64) #VARCHAR(64)
    modelo = models.CharField(max_length=64) #VARCHAR(64)
    quantidade_de_tiros = models.PositiveIntegerField #INT
    valor_estimado = models.DecimalField(max_digits = 30, decimal_places=15) #DOUBLE
    imagem = models.CharField(max_length=128) #VARCHAR(128)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Municao(models.Model):
    #objects = ArmasManager()
    #Para instanciar o objeto: municao = Municao.objects.criar_municao

    id = models.OneToOneField("Objeto", primary_key=True, on_delete=models.CASCADE) #BIGINT
    calibre_id = models.ForeignKey("Calibre", on_delete=models.SET_NULL, null=True) #SMALLINT
    marca = models.CharField(max_length=64) #VARCHAR(64)
    modelo = models.CharField(max_length=64) #VARCHAR(64)
    valor_estimado = models.DecimalField(max_digits = 30, decimal_places=15) #DOUBLE

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)