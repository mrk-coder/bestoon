from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/expense/$', views.submit_expense, name='submit_expense'),
    url(r'^submit/income/$', views.submit_income, name='submit_income'),
    url(r'^accounts/register_api/$', views.register_api, name='register_api'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/log_in/$', views.log_in, name='log_in'),
    url(r'^accounts/log_in_api/$', views.log_in_api, name='log_in_api')
]

