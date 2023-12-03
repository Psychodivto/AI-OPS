import graphene

from graphene_django.types import DjangoObjectType

from graphene import relay

from autos.models import Auto, Propietario


class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        fields = (
            "id",
            "nombre",
            "apellido",
            "fecha_nacimiento",
            "email",
            "telefono",
            "direccion",
        )

class AutoType(DjangoObjectType):

    propietario= graphene.Field(PropietarioType)

    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "color", "matricula", "anio", "imagen_url")

class AutosConnection(relay.Connection):
    class Meta:
        node = AutoType

class Query(graphene.ObjectType):
    all_autos = graphene.List(AutoType)
    marca_auto = graphene.Field(AutoType, marca=graphene.String())
    matricula_auto = graphene.Field(AutoType, matricula=graphene.String())
    

    def resolve_all_autos(self, info, **kwargs):
        return Auto.objects.all()
        for auto in autos:
            auto.propietario = auto.propietario.nombre_completo()
        return autos

    def resolve_marca_auto(self, info, **kwargs):
        marca = kwargs.get("marca")
        if marca is not None:
            return Auto.objects.get(marca=marca)
        return None

    def resolve_matricula_auto(self, info, **kwargs):
        matricula = kwargs.get("matricula")
        if matricula is not None:
            return Auto.objects.get(matricula=matricula)
        return None

class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    color = graphene.String()
    matricula = graphene.String()
    anio = graphene.Int()
    imagen_url = graphene.String()

    class Arguments:
        marca = graphene.String()
        modelo = graphene.String()
        color = graphene.String()
        matricula = graphene.String()
        anio = graphene.Int()
        imagen_url = graphene.String()

    def mutate(self, info, marca, modelo, color, matricula, anio, imagen_url):
        auto = Auto(marca=marca, modelo=modelo, color=color, matricula=matricula, anio=anio, imagen_url=imagen_url)
        auto.save()

        

        return CreateAuto(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            color=auto.color,
            matricula=auto.matricula,
            anio=auto.anio,
            imagen_url=auto.imagen_url,
        )


class DeleteAuto(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        auto = Auto.objects.get(pk=id)
        auto.delete()

        return DeleteAuto(id=id)

class UpdateAuto(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    color = graphene.String()
    matricula = graphene.String()
    anio = graphene.Int()
    imagen_url = graphene.String()

    class Arguments:
        id = graphene.Int()
        marca = graphene.String()
        modelo = graphene.String()
        color = graphene.String()
        matricula = graphene.String()
        anio = graphene.Int()
        imagen_url = graphene.String()

    def mutate(self, info, id, marca, modelo, color, matricula, anio, imagen_url):
        auto = Auto.objects.get(pk=id)
        auto.marca = marca
        auto.modelo = modelo
        auto.color = color
        auto.matricula = matricula
        auto.anio = anio
        auto.imagen_url = imagen_url
        auto.save()

        return UpdateAuto(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            color=auto.color,
            matricula=auto.matricula,
            anio=auto.anio,
            imagen_url=auto.imagen_url,
        )    

class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()
    delete_auto = DeleteAuto.Field()
    update_auto = UpdateAuto.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)