from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'common.views.index', name='index'),
    url(r'^profile$', 'common.views.user_profile', name="user_profie"),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^reset-password$','django.contrib.auth.views.password_reset'),
    url(r'^register$','common.views.register', name="register"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
