from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_member', add_member, name='add_member'),
    path('update_member/<int:id>', update_member, name='update_member'),
    path('delete_member/<int:id>', delete_member, name='delete_member'),
    path('search_members/', search_members, name='search_members'),
    path('reports/', generate_report, name='reports'),
    path('due-members/', due_members, name='due_members'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)