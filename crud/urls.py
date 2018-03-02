from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^specialization$', views.spec_list_all, name='spec_list_all'),
    url(r'^specialization/new$', views.spec_new, name='spec_new'),
    url(r'^specialization/edit/(?P<spec_id>[0-9]+)/$', views.spec_edit, name='spec_edit'),
    url(r'^specialization/save/$', views.spec_save, name='spec_save'),
    url(r'^specialization/delete$', views.spec_delete, name='spec_delete'),

    url(r'^ajax/specialization$', views.ajax_spec_list_all, name='ajax_spec_list_all'),
    url(r'^ajax/specialization/delete$', views.ajax_spec_delete, name='ajax_spec_delete'),

    url(r'^character$', views.char_list_all, name='char_list_all'),
    url(r'^character/new$', views.char_new, name='char_new'),
    url(r'^character/edit/(?P<char_id>[0-9]+)/$', views.char_edit, name='char_edit'),
    url(r'^character/save/$', views.char_save, name='char_save'),
    url(r'^character/delete$', views.char_delete, name='char_delete'),

    url(r'^ajax/character$', views.ajax_char_list_all, name='ajax_char_list_all'),
    url(r'^ajax/character/delete$', views.ajax_char_delete, name='ajax_char_delete')
]