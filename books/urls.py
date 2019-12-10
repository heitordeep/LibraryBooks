from django.contrib.auth import views as auth_views
from django.urls import path
from books.views import IndexView, CreateStudent, DeleteStudent, \
                        UpdateStudent, DetailStudent, CreateBooks


app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new_student/', CreateStudent.as_view(), name='create_students'),
    path('delete/<pk>/', DeleteStudent.as_view(), name='delete_student'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update_student/<pk>/',
         UpdateStudent.as_view(), name='update_student'),
    path('detail_student/<pk>/',
         DetailStudent.as_view(), name='detail_student'),
    path('create_books/', CreateBooks.as_view(), name='create_books'),
]
