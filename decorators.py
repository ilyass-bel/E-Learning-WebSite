from django.http import HttpResponse
from django.shortcuts import redirect


def utilisateurs_autorises(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('vous n\'êtes pas autorisé à consulter cette page')
        return wrapper_func
    return decorator