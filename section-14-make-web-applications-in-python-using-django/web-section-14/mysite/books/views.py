from django.views import generic
from django.views.generic.edit import CreateView

from .models import Book
class IndexListView(generic.ListView):
    template_name = "books/index.html"

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model = Book
    template_name = "books/detail.html"

class BookCreateView(CreateView):
    model = Book
    fields = [
        'name','author','price',
        'type','year','book_image'
    ]
    template_name = "books/book_form.html"
