from django.urls import include, path
from quickstart import views
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include("quickstart.urls")),
    path('admin/', admin.site.urls)
]