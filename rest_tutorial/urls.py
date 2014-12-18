# from django.conf.urls import patterns, include, url
# from rest_framework import routers
# from quickstart import views

from django.contrib import admin
admin.autodiscover()


from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]



#Commented b'coz /users/ using view of quickstart app
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     url(r'^', include('snippets.urls')),
# ]

# urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^', include('snippets.urls')),

# )

# urlpatterns += [
    # url(r'^api-auth/', include('rest_framework.urls',
                               # namespace='rest_framework')),    #Provides the login button in API
# ]
