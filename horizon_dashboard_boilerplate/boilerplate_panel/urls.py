from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from horizon_dashboard_boilerplate.boilerplate_panel import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^dummy_data/$',
        views.JSONView.as_view(), name='dummy_data'),
)
