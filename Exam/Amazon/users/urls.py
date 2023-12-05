from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('shop_now/', shopnow, name='shop_now'),
    path('explore_more/', ExploreMore, name='explore_more'),
    path('see_all_deals/', SeeAllDeal, name='see_all_deals'),

    path('see_more/', SeeMore, name='see_more'),
    path('laptops/', laptops, name='laptops'),
    path('toys/', Toys, name='toys'),
    path('atthemoment/', AtTheMoment, name='atthemoment'),
    path('product_books/', ProductBook, name='product_books'),
    path('drinks/', ProductDrinks, name='drinks'),
    path('CocaCola/', CocaCola, name='CocaCola'),
    path('Pepsi/', Pepsi, name='Pepsi'),
    path('Sprite/', Sprite, name='Sprite'),




    path('perfume/', Perfume, name='perfume'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('send_email/', send_email, name='send_email')

]