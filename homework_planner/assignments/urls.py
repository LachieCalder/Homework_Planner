from django.conf.urls import patterns, url
from .views import AssignmentView

urlpatterns = patterns('',
	url('^$', AssignmentView.as_view()),
)
