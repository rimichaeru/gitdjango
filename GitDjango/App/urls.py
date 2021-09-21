from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import details

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('account/details', details, name="details"),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
