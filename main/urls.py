from django.urls import path
from .views import *

    

urlpatterns = [

    path("",index,name="index"),
    path("dashboard",dashboard,name="dashboard"),

    path("about",about,name="about"),
    path("contact_us",contact_us,name="contact_us"),

    path("signin",signin,name="signin"),
    path("signup",signup,name="signup"),

    path("signout",signout,name="signout"),
    path("verify_otp",verify_otp,name="verify_otp"),

    path("resend_otp",resend_otp,name="resend_otp"),

    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),

    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),

    path('package/<str:package_name>',package,name="package"),
    path('privacy_policy',privacy_policy,name="privacy_policy"),
    
    path('generate_invoice/<int:id>',generate_invoice,name="generate_invoice"),
    
    # My account
    
    path("my-account/my_cart",my_cart,name="my_cart"),
    path('delete-cart/<int:item_id>/', delete_cart, name='delete_cart'),

    path("my-account",my_account,name="my_account"),
    path("my-account/orders",orders,name="orders"),
    path("my-account/downloads",downloads,name="downloads"),
    path("my-account/billing-address",user_billing_address,name="user_billing_address"),
    path("my-account/account-details",account_details,name="account_details"),
    path("my-account/checkout",checkout,name="checkout"),
    path("my-account/view_order/<str:ord_id>",view_order,name="view_order"),
    path("my-account/edit-billing-address",edit_billing_address,name="edit_billing_address"),
    path("my-account/customer-query",user_customer_query,name="user_customer_query"),
    
    path('payment/<int:order_id>/', payment_page, name='payment_page'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),
    path('update-order-status/', update_order_status, name='update_order_status'),


    
    
    
    
    
    
    # Admin dashboard
    
    path('admin/dashboard',dashboard,name="dashboard"),
    path('admin/order-dashboard',order_dashboard,name="order_dashboard"),
    path('admin/orders-list',orders_list,name="orders_list"),
    path('admin/admin-view-order/<int:id>',admin_view_order,name="admin_view_order"),
    path('admin/customer-query',customer_query,name="customer_query"),
    path('admin/upload-report/<int:id>',upload_report,name="upload_report"),
    path('admin/users_list',users_list,name="users_list"),
    path('admin/billing-address',billing_address,name="billing_address"),
    path('admin/contact-us',contact_list,name="contact_list")
]
















