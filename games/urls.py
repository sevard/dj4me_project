from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'games'
urlpatterns = [
    path('', TemplateView.as_view(template_name='games/index.html'), name='games-index'),
    path('<slug:guess>', views.GameView.as_view())
]
