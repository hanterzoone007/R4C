from django import template

register = template.Library()

@register.simple_tag
def create_form():
    text = '<form>'
    for i in range(3):
        text+=f'<input>'
    text+='</form>'
    return text