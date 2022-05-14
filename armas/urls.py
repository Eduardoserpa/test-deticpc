from django.urls import include, path
from .views import * #Arma, Municao, Objeto, Calibre, Objeto_tipo
from armas import views

# Padrões de URL para acessar operações CRUD ou para retornar lista de objetos
urlpatterns = [
    path('', views.index, name='index'),

    path('create-arma/', ArmaCreate.as_view(), name='create-arma'),
    path('arma/<int:id>/', ArmaDetail.as_view(), name='retrieve-arma'),
    path('update/<int:id>/', ArmaUpdate.as_view(), name='update-arma'),
    path('delete/<int:id>/', ArmaDelete.as_view(), name='delete-arma'),

    path('create-municao/', MunicaoCreate.as_view(), name='create-municao'),
    path('municao/<int:id>/', MunicaoDetail.as_view(), name='retrieve-municao'),
    path('update/<int:id>/', MunicaoUpdate.as_view(), name='update-municao'),
    path('delete/<int:id>/', MunicaoDelete.as_view(), name='delete-municao'),


    path('list-arma', ArmaList.as_view()),
    path('list-municao', MunicaoList.as_view()),
    path('list-objeto', ObjetoList.as_view()),
    path('list-calibre', CalibreList.as_view()),
    path('list-objeto-tipo', Objeto_tipoList.as_view())
]
