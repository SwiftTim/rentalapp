from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =  [
    path('', views.homepage, name='homepage'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('properties/<int:id>/book/', views.book_property, name='book_property'),
    path('services/', views.services, name='services'),  # Correct path for services page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)