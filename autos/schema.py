import graphene

from graphene import relay

from graphene_django import DjangoObjectType

from .models import Auto

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "color", "matricula", "ano", "imagen_url")


class AutosConnection(relay.Connection):
    class Meta:
        node = AutoType

class Query(graphene.ObjectType):
    autos = graphene.List(AutoType)
    autos_by_marca = graphene.List(AutoType, marca=graphene.String(required=True))
    paginate_autos = relay.ConnectionField(AutosConnection)

    def resolve_paginate_autos(self, info, **kwargs):
        return Auto.objects.all()

    def resolve_autos_by_marca(self, info, marca):
        return Auto.objects.filter(marca=marca)

    def resolve_autos(self, info, **kwargs):
        return Auto.objects.all()



class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    color = graphene.String()
    matricula = graphene.Int()
    ano = graphene.Int()
    imagen_url = graphene.String()

    class Arguments:
        marca = graphene.String(required=True)
        modelo = graphene.String(required=True)
        color = graphene.String(required=True)
        matricula = graphene.Int()
        ano = graphene.Int()
        imagen_url = graphene.String(required=True)

    ok = graphene.Boolean()
    autos = graphene.Field(AutoType)

    def mutate(self, info, marca, modelo, color, matricula, ano, imagen_url):
        auto=Auto(marca=marca, modelo=modelo, color=color, matricula=matricula, ano=ano, imagen_url=imagen_url)

        auto.save()
        ok = True

        return CreateAuto(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            color=auto.color,
            matricula=auto.matricula,
            ano=auto.ano,
            imagen_url=auto.imagen_url,
        )

class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()
