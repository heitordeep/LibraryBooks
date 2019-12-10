from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import FormStudent, UpdateForm, FormBooks
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from books.models import Student, Category, Books
from datetime import date, timedelta


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class IndexView(generic.ListView):

    template_name = 'books/index.html'
    context_object_name = 'contacts'
    paginate_by = 4
    model = Student

    def get_queryset(self):

        query = self.request.GET.get('search')
        students = Student.objects.all()

        if query:
            students = students.filter(name__icontains=query)
        return students


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class DeleteStudent(SuccessMessageMixin, generic.DeleteView):
    template_name = 'books/delete.html'
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('books:index')
    success_message = 'Estudante excluido com sucesso'


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class UpdateStudent(SuccessMessageMixin, generic.UpdateView):
    template_name = 'books/update_student.html'
    model = Student
    form_class = UpdateForm
    success_url = reverse_lazy('books:index')
    success_message = 'Atualizado com sucesso'


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class CreateStudent(SuccessMessageMixin, generic.CreateView):
    template_name = 'books/create_student.html'
    model = Student
    form_class = FormStudent
    success_url = reverse_lazy('books:index')
    success_message = 'Cadastrado com sucesso'


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class CreateBooks(SuccessMessageMixin, generic.CreateView):
    template_name = 'books/create_books.html'
    model = Books
    form_class = FormBooks
    success_url = reverse_lazy('books:index')
    success_message = 'Livro cadastrado com sucesso'


@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class DetailStudent(generic.DetailView):
    template_name = 'books/detail_student.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = date.today()
        context['date'] = get_object_or_404(Student, pk=self.kwargs['pk'])
        context['birth_of_date'] = context['date'].birth_date
        context['year'] = timedelta(days=365)
        context['result'] = int(
            abs((context['birth_of_date'] - context['now']) / context['year']))
        return context
