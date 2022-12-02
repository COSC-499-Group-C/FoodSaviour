from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .models import OrgGroups


def registered_org_user(function):
    def wrap(request, *args, **kwargs):
        if request is not None and request.user.is_authenticated:
            if OrgGroups.objects.filter(user_id=request.user.id).exists():
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            return redirect("/login")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
