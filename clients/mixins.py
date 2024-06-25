
from django.contrib.auth.models import Group

# Se importa el mixin de autenticacion y validacion de grupos de el proyecto aurora_api
from aurora_api.mixins import GroupMemberMixin


class BasculaGroupMemberMixin(GroupMemberMixin):
    # grupos existentes en la base de datos
    
    """
    
    """
    bascula_group = Group.objects.get(name='Bascula')
    allowed_groups = [bascula_group.name]



