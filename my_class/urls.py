from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name="my_class"

urlpatterns = [
	path('',homepage),

	path('profiles/sign_up',sign_up),
	path('profiles/sign_in',sign_in),
	path('profiles/<int:pk>',profile),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)