from django.conf.urls import url
from bookapp import views
app_name = 'bookapp'

urlpatterns =[
    url('book/',views.book_details,name="book"),
    url('author/',views.author_details,name="author"),
    url('product/',views.product_details,name="product"),
    url('cart/',views.add_cart,name="cart"),
    url('mobile/',views.mobile,name="mobile"),
    url('mobile_get/',views.mobile_get,name="mobile_get"),
    url('mobile_delete/',views.mobile_delete,name="mobile_get"),
    url('all_list/',views.all_list,name="all_list")
]