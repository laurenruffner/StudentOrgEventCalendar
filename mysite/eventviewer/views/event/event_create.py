from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from eventviewer.models import Event

class eventCreateView(CreateView):
    model = Event
    fields = '__all__'
    template_name = "event/event_create.html"
    success_url = reverse_lazy('event_list')
