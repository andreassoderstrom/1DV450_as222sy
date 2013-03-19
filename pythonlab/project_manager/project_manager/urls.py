from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^projects/$', 'projectmanager.views.project_list', name='project_list'), #list of projects
    url(r'^projects/(?P<project_id>\d+)/$', 'projectmanager.views.project_list', name='project'), #single project
    url(r'^projects/add$', 'projectmanager.views.project_add', name='project_add'), #add a project
    url(r'^projects/(?P<project_id>\d+)/delete/$', 'projectmanager.views.project_delete', name='project_delete'), #delete project
    url(r'^projects/(?P<project_id>\d+)/edit/$', 'projectmanager.views.project_edit', name='project_edit'), #edit project

    url(r'^projects/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)$', 'projectmanager.views.ticket', name='ticket'), #single ticket
    url(r'^projects/(?P<project_id>\d+)/ticket/add$', 'projectmanager.views.ticket_add', name='ticket_add'), #add a ticket
    url(r'^projects/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)/edit/$', 'projectmanager.views.ticket_edit', name='ticket_edit'), #edit ticket
    url(r'^projects/(?P<project_id>\d+)/ticket/(?P<ticket_id>\d+)/delete/$', 'projectmanager.views.ticket_delete', name='ticket_delete'), #delete ticket


    url(r'^login/$', 'projectmanager.views.login_user', name='login'), # log in

    url(r'^logout/$', 'projectmanager.views.logout_user', name='logout'), # log out
    #url(r'^projects/(?P<project_id>\d+)/delete/$', 'projectmanager.views.project_delete', name='project_delete'),
    #url(r'^projects/(?P<project_id>\d+)/edit/$', 'projectmanager.views.project_edit', name='project_edit'),

    # url(r'^project_manager/', include('project_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
