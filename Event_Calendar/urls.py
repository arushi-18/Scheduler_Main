from django.urls import path
from . import views

urlpatterns=[
    path('events/<str:username>/',views.CalendarView.as_view(),name="event"),
    path('new/',views.event,name="event_new"),
    path('edit/<int:event_id>/',views.event,name="event_edit"),
]