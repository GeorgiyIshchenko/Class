from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name="my_class"

urlpatterns = [
	path('',homepage),

	path('sign_up',sign_up),
	path('sign_in',sign_in),
	path('im',profile),
	path('edit',edit_profile),
	path('logout', logout)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)