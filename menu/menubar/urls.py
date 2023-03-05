from django.urls import path

from menubar.views import HomeView, AboutView


urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view())
]
