from django.forms import ChoiceField, FileField

from django import template
register = template.Library()


@register.filter(name='field_value')
def field_value(field):
    """
    Returns the value for this BoundField, as rendered in widgets.

    From: https://code.djangoproject.com/ticket/10427
    """
    if field.form.is_bound:
        if isinstance(field.field, FileField) and field.data is None:
            val = field.form.initial.get(field.name, field.field.initial)
        else:
            val = field.data
    else:
        val = field.form.initial.get(field.name, field.field.initial)
        if callable(val):
            val = val()
    if val is None:
        val = ''
    return val


@register.filter(name='display_value')
def display_value(field):
    """
    Returns the displayed value for this BoundField, as rendered in widgets.

    This won't work correctly if your choice values are a mix of int and str (and could potentially overlap).

    Based on: https://code.djangoproject.com/ticket/10427
    (but modified to support int choices)
    """

    # normalize current value to str (in case form.initial is an int)
    current_val = str(field_value(field))
    if isinstance(field.field, ChoiceField):
        for (choice_val, choice_desc) in field.field.choices:
            # normalize choice values to str to match submitted value (always str)
            if str(choice_val) == current_val:
                return choice_desc
    return current_val
