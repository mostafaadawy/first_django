from django.urls import path
from .views import (
    my_fbv,
    # courseDeleteView,
    # courseDetailView,
    # courseListView,
    # courseUpdateView,


)

app_name = 'courses'
urlpatterns = [
    path('', my_fbv, name='course-list'),
    # path('', courseListView.as_view(), name='course-list'),
    # path('create/', courseCreateView.as_view(), name='course-create'),
    # path('<int:id>/', courseDetailView.as_view(), name='course-detail'),
    # path('<int:id>/update/', courseUpdateView.as_view(), name='course-update'),
    # path('<int:id>/delete/', courseDeleteView.as_view(), name='course-delete'),
]
