from django.urls import path

from django.contrib.auth import views  as auth_views

from . import views

urlpatterns = [ 
    path('register/', views.registrationPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user_page"),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products, name="products"),
    path('tags/', views.tags, name="tags"),
    path('customers/<str:pk>', views.customer, name="customers"),
    
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>', views.deleteProduct, name="delete_product"),
    
    path('create_tag/', views.createTag, name="create_tag"),
    path('update_tag/<str:pk>', views.updateOrder, name="update_tag"),
    path('delete_tag/<str:pk>', views.deleteOrder, name="delete_tag"),
    
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>', views.deleteCustomer, name="delete_customer"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset/password_reset_done.html"), name="password_reset_complete"),
    
]
