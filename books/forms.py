from django.forms import ModelForm, TextInput, Select, DateInput
from .models import Student, Books

# Form de criação de livros.


class FormBooks(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'category']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da categoria'}),
            'category': Select(attrs={'class': 'form-control'}),
        }

# Form cadastro de aluguel de livros.


class FormStudent(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'cpf', 'birth_date',
                  'city', 'email', 'tel', 'book']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'cpf': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
            'birth_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua cidade'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'}),
            'tel': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone'}),
            'book': Select(attrs={'class': 'form-control'}),

        }

# Form Upgrade cadastro estudante.


class UpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'tel', 'book']

        widgets = {
            'book': Select(attrs={'class': 'form-control'}),
        }
