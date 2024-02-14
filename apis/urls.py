from django.urls import path

from .views import weather, menu ,image

urlpatterns = [
    path('weather/', weather.WeatherView.as_view()),
    #path('menu/', menu.get_menu, name='menu'),
    #path('image', image.image, name='image'),
    #path('imagetext', image.image_text, name='image_text'),
    path('image', image.ImageView.as_view())
]