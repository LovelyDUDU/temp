from django.contrib import admin
from django.urls import path
import BBapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BBapp.views.index, name="index"),
    path('detail/<int:post_id>', BBapp.views.detail, name="detail"),
    path('write/', BBapp.views.write, name="write"),
    path('update/<int:post_id>', BBapp.views.update, name="update"),
    path('delete/<int:post_id>', BBapp.views.delete, name="delete"),
    path('search/', BBapp.views.search, name="search"),
    path('category/', BBapp.views.category, name="category"),
    path('signup/', accounts.views.signup, name="signup"),
    path('login/', accounts.views.login, name="login"),
    path('logout/', accounts.views.logout, name='logout'),
]
