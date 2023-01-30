from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView
# from products.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view, product_update_view, product_list_view
app_name = 'articles'
urlpatterns = [
    path('', ArticleListView, name='list'),
    path('create/', ArticleCreateView, name="create"),
    path('<int:my_id>/', ArticleDetailView, name="detail"),
    # path('<int:my_id>/delete/', product_delete_view, name="delete"),
    # path('<int:my_id>/update/', product_update_view, name="update"),
]
