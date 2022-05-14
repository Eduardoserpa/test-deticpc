from django.shortcuts import render
from .models import * #Arma, Municao, Objeto, Calibre, Objeto_tipo
from rest_framework import generics
from .serializers import * #Arma, Municao, Objeto, Calibre, Objeto_tipo

# Endpoints de API: CRUD para objetos individuais + lista de objetos por classe
# CRUD completo: Arma
class ArmaCreate(generics.CreateAPIView):

    queryset1 = Arma.objects.all(),
    serializer_class = ArmaSerializer

    #queryset2 = Objeto.objects.all(),
    #serializer_class2 = ObjetoSerializer

class ArmaDetail(generics.RetrieveAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class ArmaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class ArmaDelete(generics.RetrieveDestroyAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


# CRUD completo: Municao
class MunicaoCreate(generics.CreateAPIView):
    queryset1 = Municao.objects.all(),
    serializer_class = MunicaoSerializer

    #queryset2 = Objeto.objects.all(),
    #serializer_class2 = MunicaoSerializer

class MunicaoDetail(generics.RetrieveAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer

class MunicaoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer

class MunicaoDelete(generics.RetrieveDestroyAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer


# READ em lista: Objeto, Arma, Municao, Calibre, Objeto_tipo
class ArmaList(generics.ListAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class MunicaoList(generics.ListAPIView):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer

class ObjetoList(generics.ListAPIView):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer

class CalibreList(generics.ListAPIView):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer

class Objeto_tipoList(generics.ListAPIView):
    queryset = Objeto_tipo.objects.all()
    serializer_class = Objeto_tipoSerializer

def index(request):
    num_armas = Arma.objects.all().count()
    num_municao = Municao.objects.all().count()

    context = {
        'num_armas': num_armas,
        'num_municao': num_municao,
    }

    return render(request, 'index.html', context=context)
