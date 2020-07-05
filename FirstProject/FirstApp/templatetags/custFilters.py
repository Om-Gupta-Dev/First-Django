from django import template

register = template.Library()

@register.filter(name = 'first20')          #registering using decorators
def first20(value):
    output = value[:20]
    return output

def first_n(value,n):
    output = value[:n]
    return output

register.filter('first_n' , first_n)        #Simple register