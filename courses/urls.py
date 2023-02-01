from django.urls import path
from .views import (
    # my_fbv,
    CourseView,
    CourseListView,
    CourseUpdateView,
    CourseCreateView,
    # courseUpdateView,


)

app_name = 'courses'
urlpatterns = [
    # path('', my_fbv, name='course-list'),
    # path('', CourseView.as_view(template_name="contact.html"), name='course-list'),
    path('', CourseListView.as_view(), name='course-list'),
    # path('', MyListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    # path('<int:id>/delete/', courseDeleteView.as_view(), name='course-delete'),
]
