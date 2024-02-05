import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.db import models
from sistema.models import Auto, Propietario

class AutoFilter(django_filters.FilterSet):
    imagen = django_filters.CharFilter(lookup_expr='icontains')  # Utiliza lookup_expr directamente

    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'anio', 'matricula', 'color', 'adquisicion', 'imagen']

class PropietarioFilter(django_filters.FilterSet):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'dni', 'direccion', 'telefono', 'email', 'auto' ]

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        interfaces = (graphene.relay.Node, )

class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        interfaces = (graphene.relay.Node, )

class RelayQuery(graphene.ObjectType):
    relay_auto = graphene.relay.Node.Field(AutoType)
    relay_autos = DjangoFilterConnectionField(AutoType, filterset_class=AutoFilter)
    relay_propietario = graphene.relay.Node.Field(PropietarioType)
    relay_propietarios = DjangoFilterConnectionField(PropietarioType, filterset_class=PropietarioFilter)
