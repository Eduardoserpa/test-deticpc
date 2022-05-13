from rest_framework import serializers
from .models import * #Arma, Municao, Objeto, Calibre, Objeto_tipo

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = ['id', 'objeto_tipo_id']

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ['id', 'calibre_id', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem']

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = ['id', 'calibre_id', 'marca', 'modelo', 'valor_estimado']

class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = ['id', 'desc_calibre']

class Objeto_tipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_tipo
        fields = ['id', 'tipo_de_objeto']