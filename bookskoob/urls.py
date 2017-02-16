"""bookskoob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from books.views import ViewAllBooks, BookAddGeneric, BookUpdateGeneric, BookDeleteGeneric, LogsView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login', logout_then_login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^log/$', logout_then_login, name='login-logout'),
    url(r'^/?$', ViewAllBooks.as_view(), name='all-books'),
    url(r'^new/?$', BookAddGeneric.as_view(), name='book-new'),
    url(r'^book_edit/(?P<pk>\d+)/?$', BookUpdateGeneric.as_view(), name='book-edit'),
    url(r'^book_delete/(?P<pk>\d+)/?$', BookDeleteGeneric.as_view(), name='book-delete'),
    url(r'^history/?$', LogsView.as_view(), name='history'),
]
