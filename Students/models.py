from django.db import models

# Create your models here.

class StudentGroup(models.Model):
    group_number = models.CharField(max_length=10, unique=True)
    motto = models.CharField(max_length=100, blank=True, null=True)
    meeting_cabinet = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Група: {self.group_number}"


class UniversityStudent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_card_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_card_number})"


class LibraryCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    student = models.OneToOneField(UniversityStudent, on_delete=models.CASCADE)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Бібліотечна карта: {self.card_number} ({self.student})"


class LibraryLiterature(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField()
    year = models.PositiveIntegerField()
    author = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class BookBorrowingProcess(models.Model):
    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
    literature = models.ForeignKey(LibraryLiterature, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    librarian_full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Книга '{self.literature.title}' взята по карті {self.library_card.card_number} ({self.borrow_date})"
