from django.conf.urls import  include, url
from django.urls import path
from django.contrib import admin
import django.contrib.auth.views


from django.contrib import admin

import common.views
#import common.views.user_profile
#import common.views.register


urlpatterns = [
    url(r'^$', common.views.index, name='index'),
    url(r'^profile$', common.views.user_profile, name="user_profile"),
    #django.contrib.auth.views.login

    url(r'^login$', django.contrib.auth.views.LoginView,  {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout$', django.contrib.auth.views.LogoutView, {"next_page": "login"}, name='logout'),
    url(r'^reset-password$',django.contrib.auth.views.PasswordResetView, name='reset-password'),
    url(r'^reset-password-done$',django.contrib.auth.views.PasswordResetDoneView, name="password_reset_done"),
    url(r'^password-confim/(?P<uidb64>.+)/(?P<token>.+)/$', django.contrib.auth.views.PasswordResetConfirmView, name='password_reset_confirm'),
    url(r'^reset-password-complete', django.contrib.auth.views.PasswordResetCompleteView, name='password_reset_complete'),
    url(r'^register$',common.views.register, name="register"),
    # url(r'^blog/', include('blog.urls')),

    path(r'^admin/', admin.site.urls),
]

