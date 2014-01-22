from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'common.views.index', name='index'),
    url(r'^profile$', 'common.views.user_profile', name="user_profile"),
    url(r'^login$', 'django.contrib.auth.views.login',  name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {"next_page": "login"}, name='logout'),
    url(r'^reset-password$','django.contrib.auth.views.password_reset', name='reset-password'),
    url(r'^reset-password-done$','django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    url(r'^password-confim/(?P<uidb64>.+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^reset-password-complete', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^register$','common.views.register', name="register"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
