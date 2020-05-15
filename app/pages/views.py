from django.views.generic import FormView, TemplateView
import requests

from .forms import CreatePostForm, RequestPostForm


class PagesView(TemplateView):
    template_name = 'pages/home.html'


class GetView(FormView):

    template_name = 'pages/get.html'

    form_class = RequestPostForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(GetView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print("Valid Post Method Called")
        # This method is called when valid form data has been POSTed.

        # Proccess the form to send to the Rest API on the api:8888 container
        # This is an empty form. Nothing to process.

        url = "http://api:8888"

        payload = {}
        headers = {
        }

        # In order to use a validation token:
        # https://github.com/PwnSauceDesigns/fundraiser_app/blob/master/fundraiser_app/views.py
        # https://stackoverflow.com/questions/55500246/django-send-a-post-request-through-form-to-another-server/55502006
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))
        print(response.json())

        # It should return an HttpResponse.
        return super(GetView, self).form_valid(form)


class PostView(FormView):

    template_name = 'pages/post.html'

    form_class = CreatePostForm
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
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

        # In order to use a validation token:
        # https://github.com/PwnSauceDesigns/fundraiser_app/blob/master/fundraiser_app/views.py
        # https://stackoverflow.com/questions/55500246/django-send-a-post-request-through-form-to-another-server/55502006
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text.encode('utf8'))
        print(response.json())

        # It should return an HttpResponse.
        return super(PostView, self).form_valid(form)
