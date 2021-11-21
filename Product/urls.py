from django.urls import path

from . import views

urlpatterns = [
    #path('home/', views.contentview, name='prod-home'),
    path('', views.list_view.as_view(), name='prod-home'),
    path('create/', views.createview, name='prod-create'),
    path('<int:id>/delete/', views.delete_view.as_view(), name='prod-delete'),
    path('<int:pk>/comment/delete/', views.delete_comment, name='comment-delete'),
    path('<int:id>/update/', views.update_view.as_view(), name='prod-update'),
    path('search/', views.search_view, name='prod-search'),
    path('product/', views.content_view, name='prod-product'),
    path('create_pdf/', views.pdf_report_create, name='create-pdf'),
    path('about/', views.aboutview, name='product-about'),
    path('<int:id>/detail/', views.detail_view.as_view(), name='prod-detail'),
]