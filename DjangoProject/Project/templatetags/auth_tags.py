from django import template

register = template.Library()


@register.filter(name='get_user_type')
def get_user_type(user):
    print(user.id)
