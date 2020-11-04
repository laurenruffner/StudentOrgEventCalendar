from eventviewer.views import eventDeleteView
from eventviewer.views import eventUpdateView
from eventviewer.views import eventDetailView
from eventviewer.views import eventCreateView
from eventviewer.views import eventListView
from eventviewer.views import OrganizationDeleteView
from eventviewer.views import OrganizationUpdateView
from eventviewer.views import OrganizationDetailView
from eventviewer.views import OrganizationCreateView
from eventviewer.views import OrganizationListView
from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('organization/list/', OrganizationListView.as_view(), name='organization_list'),
    path('organization/create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('organization/detail/<int:pk>/', OrganizationDetailView.as_view(), name='Organization_detail'),
    path('organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='Organization_update'),
    path('organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='Organization_delete'),

    path('event/list/', eventListView.as_view(), name='event_list'),
    path('event/create/', eventCreateView.as_view(), name='event_create'),
    path('event/detail/<int:pk>/', eventDetailView.as_view(), name='event_detail'),
    path('event/update/<int:pk>/', eventUpdateView.as_view(), name='event_update'),
    path('event/delete/<int:pk>/', eventDeleteView.as_view(), name='event_delete')
]