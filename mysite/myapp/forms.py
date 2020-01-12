from django import forms


class MyForm(forms.Form):
    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )
    category = forms.ChoiceField(choices=CHOICES, initial=11)
