from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views

from django.contrib import admin
admin.autodiscover()


#Commented b'coz /users/ using view of quickstart app
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     url(r'^', include('snippets.urls')),
# ]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),

)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),    #Provides the login button in API
]
