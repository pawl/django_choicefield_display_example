This repo demonstrates how to get the display text of the current selection for a django ChoiceField.

It's easy to get a ChoiceField's currently selected value using `form.field.value`, but it's a lot harder to get the selected value's display text.

Maybe someone can show me an easier way to do this?

## Screenshot
![screenshot](https://raw.github.com/pawl/django_choicefield_display_example/master/screenshot.png "screenshot")

## Possible Solutions

* The highest voted stackoverflow answer for getting display text for the current selection of a ChoiceField: https://stackoverflow.com/a/8428158
  * Won't work with choices that have integer values.
  * Won't show your ChoiceField's initial value on GET.
* I found some code for displaying the current selection of a ChoiceField on the django issue tracker: https://code.djangoproject.com/ticket/10427#comment:24
  * Won't work with choices that have integer values.
  * Handles initial values (even if it's a callable).
  * Handles FileFields (not sure why).

## My Solution

I ended up making a fix to handle choices with integer values to the example I found on the django issue tracker.

### Solution Components
* [form_tags.py](mysite/myapp/templatetags/form_tags.py) - (main part) The template tag for getting the current selection for a ChoiceField.
* [forms.py](mysite/myapp/forms.py) - The form with the ChoiceField.
* [view.py](mysite/myapp/view.py) - The view that redirects the form submit to the same page.
* [example.html](mysite/templates/example.html) - The html template that displays the form and uses the template tag.

### Other Thoughts

This seems like it's fairly difficult to do for what I think would be something done fairly commonly.

I know turning the ChoiceField into a ModelChoiceField and putting the choices on a CharField is one way to fix this (you can use `.get_FOO_display`), but for the purpose of this demonstration - let's pretend it's a field that doesn't make sense as a model field.

Maybe I should be making a custom django widget to do this?
