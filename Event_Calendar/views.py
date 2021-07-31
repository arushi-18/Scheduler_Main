from datetime import datetime,timedelta,date
import calendar
from calendar import HTMLCalendar
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import *
from .utils import Calendar

class CalendarView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'Event_Calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(self.request.user.username,withyear=True)
        #print(html_cal)
        #html_cal=html_cal.filter(created_by__username=self.kwargs['username'])
        context['calendar'] = mark_safe(html_cal)
        #print(context['calendar'])
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        return HttpResponseRedirect(reverse('event',kwargs={'username': request.user.username}))
    return render(request, 'Event_Calendar/event.html', {'form': form,'user':request.user})