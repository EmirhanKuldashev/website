"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import main_view, hello_view, goodbye_view, current_date_view, product_list_view, \
     product_detail_view, categories_view, product_create_view, review_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('hello/', hello_view,),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('products/', product_list_view),
    path('products/<int:product_id>/', product_detail_view),
    path('category/', categories_view),
    path('products/create/', product_create_view),
    path('', product_list_view, name='product_list'),
    path('product/<int:product_pk>/detail/', product_detail_view, name='product_detail'),
    path('product/<int:product_pk>/review/create/', review_create_view, name='review_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
