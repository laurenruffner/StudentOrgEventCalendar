from django.views.generic import ListView

from eventviewer.models import Event

class eventListView(ListView):
    model = Event
    template_name = "event/event_list.html"
