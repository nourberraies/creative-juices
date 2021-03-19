from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
						 document_root=settings.MEDIA_ROOT)