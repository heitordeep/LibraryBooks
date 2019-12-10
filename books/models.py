from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'


class Books(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Livro'


class Student(models.Model):
    name = models.CharField(max_length=70)
    cpf = models.CharField(max_length=14)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=50)
    tel = models.CharField(max_length=15)
    book= models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name='book')

    class Meta:
        verbose_name = 'Estudante'
        ordering = ['-registration_date']

    def __str__(self):
        return self.name

