from django.shortcuts import render
from books.models import Book, Logs
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# Create your views here.

class ViewAllBooks(LoginRequiredMixin, View):

    def get(self, request):
        books = Book.objects.all()

        return render(request, 'books/view_all.html', {'books': books})

    def post(self, request):
        user = request.user
        book_id = request.POST.get('click')
        action = request.POST.get('action')
        book = Book.objects.get(pk=book_id)
        if action == 'lent':
            book.available = False
            book.save()
            log = Logs.objects.create(book=book, user=user, date_get=datetime.now())
            log.save()
        elif action == 'return':
            book.available = True
            book.save()
            log = Logs.objects.create(book=book, user=user, return_date=datetime.now())
            log.save()

        books = Book.objects.all()

        return render(request, 'books/view_all.html', {'books': books})

class BookAddGeneric(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/all'

class BookUpdateGeneric(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/all'

class BookDeleteGeneric(DeleteView):
    model = Book
    fields = ['title']
    template_name_suffix = '_delete_form'
    success_url = '/all'

class BookDetailsView(DetailView):
    model = Book

class LogsView(ListView):
    model = Logs

    def get_queryset(self, **kwargs):
        if 'user' in self.kwargs:
            user = get_object_or_404(User, username=self.kwargs['user'])
        else:
            user = self.request.user
        return Logs.objects.filter(user=user)