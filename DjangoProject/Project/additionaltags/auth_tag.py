from django import template
from ..models import OrgGroups
from django.contrib.auth import authenticate

register = template.Library()


@register.simple_tag(name='get_user_type')
def get_user_type(user):
    if user is not None and user.is_authenticated:
        if OrgGroups.objects.filter(user_id=user.id).exists():
            return True
        else:
            return False
    else:
        return False
