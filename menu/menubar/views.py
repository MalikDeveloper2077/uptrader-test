from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'menubar/home.html'


class AboutView(TemplateView):
    template_name = 'menubar/about.html'
