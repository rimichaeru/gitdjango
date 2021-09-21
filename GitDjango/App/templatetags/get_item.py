from django.template.defaulttags import register


# for simultaneously accessing keys AND values in a HTML {% for loop %}
@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
