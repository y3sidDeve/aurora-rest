#AQUI IRAN LOS MIXINS GROBALES DE LA APLICACION
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect


class GroupMemberMixin(AccessMixin):
    allowed_groups = []

    def handle_no_permission(self):
        response = HttpResponseForbidden(
            "No tienes permiso para acceder a esta página."
        )
        
        return response

    def dispatch(self, request, *args, **kwargs): # el metodo se ejecuta antes de que se ejecute el metodo get, post, put, delete, etc. es parecido al metodo de javascript beforeCreate
        # Verificar si el usuario está autenticado y si pertenece a alguno de los grupos permitidos en la lista "allowed_groups".
        if not request.user.is_authenticated or not any(request.user.groups.filter(name=group) for group in self.allowed_groups):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)