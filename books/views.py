from django.shortcuts import render
from books.models import Book
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ViewAllBooks(LoginRequiredMixin, View):

    def get(self, request):
        books = Book.objects.all()

        return render(request, 'books/view_all.html', {'books': books})

class BookAddGeneric(CreateView):
    model = Book
    fields = '__all__'
    success_url = 'all'

class BookUpdateGeneric(UpdateView):
    model = Book
    fields = '__all__'
    success_url = 'all'

class BookDeleteGeneric(DeleteView):
    model = Book
    fields = ['title']
    template_name_suffix = '_delete_form'
    success_url = 'all'