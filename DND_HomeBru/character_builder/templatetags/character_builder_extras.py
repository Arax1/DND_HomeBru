from django import template

register = template.Library()

def upper(value): # Only one argument.
    """Converts a string into all uppercase"""
    return value.upper()

register.filter('upper', upper)
