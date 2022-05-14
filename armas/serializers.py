from rest_framework import serializers
from .models import * #Arma, Municao, Objeto, Calibre, Objeto_tipo

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = ['id', 'objeto_tipo_id']

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ['calibre_id', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem']
        #fields = ['id', 'calibre_id', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem']
    
    #def create(self, validated_data):
    #    objeto_serializer = ObjetoSerializer(data=validated_data.get('objeto'))
    #    objeto_serializer.is_valid()
    #    objeto_serializer.save()
    #    return Arma.objects.create(**validated_data)

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = ['calibre_id', 'marca', 'modelo', 'valor_estimado']
        #fields = ['id', 'calibre_id', 'marca', 'modelo', 'valor_estimado']
    
    #def create(self, validated_data):
    #    objeto_serializer = ObjetoSerializer(validated_data.get('objeto'))
    #    objeto_serializer.is_valid()
    #    objeto_serializer.save()
    #    return Municao.objects.create(**validated_data)

class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = ['id', 'desc_calibre']

class Objeto_tipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_tipo
        fields = ['id', 'tipo_de_objeto']
