from django.conf.urls import url
from .products import view

urlpatterns = [
    url(
        r'^api/product/$',
        view.get_post_product,
        name='get_post_product'
    )
]