
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from api.views import StudentViewSet
from api.views import StudentModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
# Creating router object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student_api', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
]
