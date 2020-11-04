from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from eventviewer.models import Event

class eventUpdateView(UpdateView):
    model = Event
    fields = '__all__'
    template_name = "event/event_update.html"
    success_url = reverse_lazy('event_list')
