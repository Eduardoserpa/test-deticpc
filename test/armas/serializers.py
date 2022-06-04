from rest_framework import serializers
from .models import * #Arma, Municao, Objeto, Calibre, Objeto_tipo

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'
        #fields = ['id', 'objeto_tipo_id']

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'
        #fields = ['id', 'calibre_id', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem']
    
    #def create(self, validated_data):
    #    objeto_serializer = ObjetoSerializer(data=validated_data.get('objeto'))
    #    objeto_serializer.is_valid()
    #    objeto_serializer.save()
    #    return Arma.objects.create(**validated_data)

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'
        #fields = ['id', 'calibre_id', 'marca', 'modelo', 'valor_estimado']
    
    #def create(self, validated_data):
    #    objeto_serializer = ObjetoSerializer(validated_data.get('objeto'))
    #    objeto_serializer.is_valid()
    #    objeto_serializer.save()
    #    return Municao.objects.create(**validated_data)

class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibre
        fields = '__all__'
        #fields = ['id', 'desc_calibre']

class Objeto_tipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto_tipo
        fields = '__all__'
        #fields = ['id', 'tipo_de_objeto']
