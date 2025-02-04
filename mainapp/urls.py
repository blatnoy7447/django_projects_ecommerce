from django.urls import path
from mainapp import AdminViews, views

urlpatterns = [
    path('admin/', views.adminLogin, name="admin_login"),
    path('admin_login_process', views.adminLoginProcess, name="admin_login_process"),
    path('admin_logout_process', views.adminLogoutProcess, name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home', AdminViews.admin_home, name="admin_home"),

    # CATEGORIES
    path('category_list', AdminViews.CategoriesListView.as_view(), name="category_list"),
    path('category_create', AdminViews.CategoriesCreate.as_view(), name="category_create"),
    path('category_update/<slug:pk>', AdminViews.CategoriesUpdate.as_view(), name="category_update"),

    # SUBCATEGORIES

    path('sub_category_list', AdminViews.SubCategoriesListView.as_view(), name="sub_category_list"),
    path('sub_category_create', AdminViews.SubCategoriesCreate.as_view(), name="sub_category_create"),
    path('sub_category_update/<slug:pk>', AdminViews.SubCategoriesUpdate.as_view(), name="sub_category_update"),

    # Merchant User
    path('merchant_create', AdminViews.MerchantUserCreateView.as_view(), name="merchant_create"),
    path('merchant_list', AdminViews.MerchantUserListView.as_view(), name="merchant_list"),
    path('merchant_update/<slug:pk>', AdminViews.MerchantUserUpdateView.as_view(), name="merchant_update"),

    # Products
    path('product_create', AdminViews.ProductView.as_view(), name="product_view"),
    path('product_list', AdminViews.ProductListView.as_view(), name="product_list"),
    path('product_edit/<str:product_id>', AdminViews.ProductEdit.as_view(), name="product_edit"),
    path('product_add_media/<str:product_id>', AdminViews.ProductAddMedia.as_view(), name="product_add_media"),
    path('product_edit_media/<str:product_id>', AdminViews.ProductEditMedia.as_view(), name="product_edit_media"),
    path('product_media_delete/<str:id>', AdminViews.ProductMediaDelete.as_view(), name="product_media_delete"),
    path('product_add_stocks/<str:product_id>', AdminViews.ProductAddStocks.as_view(), name="product_add_stocks"),
    path('file_upload', AdminViews.file_upload, name="file_upload"),

    # Staff User
    path('staff_create', AdminViews.StaffUserCreateView.as_view(), name="staff_create"),
    path('staff_list', AdminViews.StaffUserListView.as_view(), name="staff_list"),
    path('staff_update/<slug:pk>', AdminViews.StaffUserUpdateView.as_view(), name="staff_update"),

    # Customer User
    path('customer_create', AdminViews.CustomerUserCreateView.as_view(), name="customer_create"),
    path('customer_list', AdminViews.CustomerUserListView.as_view(), name="customer_list"),
    path('customer_update/<slug:pk>', AdminViews.CustomerUserUpdateView.as_view(), name="customer_update"),

]
