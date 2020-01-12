from django.views.generic.edit import FormView

from .forms import MyForm


class ExampleView(FormView):
    template_name = 'example.html'
    form_class = MyForm

    def form_valid(self, form):
        # re-render the view instead of redirecting to success_url
        return self.render_to_response(self.get_context_data())
