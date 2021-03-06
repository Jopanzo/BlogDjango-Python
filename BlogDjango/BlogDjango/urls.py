"""
Definition of urls for BlogDjango.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from blog import views as blogViews


urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('user.urls')),
    path('home/', blogViews.blog_view, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', blogViews.blog_view, name ='blog'),
    path('create/', blogViews.blog_create_view, name ='createBlog'),
    path('view/', blogViews.blog_views, name ='viewBlogs'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]