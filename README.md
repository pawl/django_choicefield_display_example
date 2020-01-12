This repo demonstrates how to get the display text of the current selection for a django ChoiceField.

![screenshot](https://raw.github.com/pawl/django_choicefield_display_example/master/screenshot.png "screenshot")

Main parts of the demonstration:
* [forms.py](mysite/myapp/forms.py) - The form with the ChoiceField.
* [view.py](mysite/myapp/view.py) - The view that redirects the form submit to the same page.
* [form_tags.py](mysite/myapp/templatetags/form_tags.py) - (main part of the solution) The template tag for getting the current selection for a ChoiceField.
* mysite/templates/example.html - The html template that displays the form and uses the template tag.

For extra difficulty, my ChoiceField has choices with integers as values. The integer values require some fixes to the template tag code I found for getting ChoiceField display values here: https://code.djangoproject.com/ticket/10427.

For even more difficult, I added an initial value to the form. This would break the main stackoverflow answer for getting display text for the current selection of a ChoiceField: https://stackoverflow.com/a/8428158

This seems like it's fairly difficult to do for what I think would be something done fairly commonly.

Maybe someone can show me an easier way to do this?

I know turning the ChoiceField into a ModelChoiceField and putting the choices on a CharField is one way to fix this (you can use `.get_FOO_display`), but for the purpose of this demonstration - let's pretend it's a field that doesn't make sense as a model field.
