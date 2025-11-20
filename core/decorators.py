from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def role_required(allowed_roles):
    """
    Verifica que el usuario tenga alguno de los roles permitidos.
    allowed_roles: lista de strings, por ejemplo ["admin", "mesero"]
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Si no está autenticado → al login
            if not request.user.is_authenticated:
                return redirect("core:login")

            # Intentar obtener el rol del perfil
            profile = getattr(request.user, "profile", None)
            role = getattr(profile, "role", None)

            # Si el rol no está permitido → 403
            if role not in allowed_roles:
                raise PermissionDenied("No tienes permiso para acceder a esta vista.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
