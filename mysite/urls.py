from django.contrib import admin
from main.views import person_create_view, person_details_view

from django.urls import path, include 

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/',include('tinymce.urls')),
    path('people/',person_create_view),
    path('person_details/',person_details_view)
]


 