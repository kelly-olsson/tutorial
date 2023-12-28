from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

# Set up the router for users and groups
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),

    # Include the Snippet app's URLs
    path('', include('snippets.urls')),

    # Include login URLs for the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# This line is no longer necessary as router.urls is already included in urlpatterns
# urlpatterns += router.urls
