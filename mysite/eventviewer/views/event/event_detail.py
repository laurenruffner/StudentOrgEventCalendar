from django.views.generic import DetailView

from eventviewer.models import Event


class eventDetailView(DetailView):
    model = Event
    template_name = "event/event_detail.html"
