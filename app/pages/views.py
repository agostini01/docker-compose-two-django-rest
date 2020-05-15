from django.views.generic import FormView
import requests

from .forms import NameForm


class PagesView(FormView):

    template_name = 'pages/home.html'

    form_class = NameForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(PagesView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print("Valid Post Method Called")
        # This method is called when valid form data has been POSTed.

        # Proccess the form to send to the Rest API on the api:8888 container
        print(form.cleaned_data['your_name'])

        url = "http://api:8888"

        payload = {}
        headers = {
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))

        # It should return an HttpResponse.
        return super(PagesView, self).form_valid(form)
