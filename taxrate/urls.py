
from django.contrib import admin
from django.urls import path
from tax.views import Calculate_tax

urlpatterns = [
    path("tax/",Calculate_tax.as_view(),name='calculate-tax'),
    path('admin/', admin.site.urls),
]
