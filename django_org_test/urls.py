from django.urls import include, path
from organizations.backends import invitation_backend

urlpatterns = [
    path('', include('polls.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('accounts/', include('organizations.urls')),
    path('invitations/', include(invitation_backend().get_urls())),
]
