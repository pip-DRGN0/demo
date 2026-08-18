from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):

    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Complaint(models.Model):

    COMPLAINT_TYPES = (
        ('Faculty', 'Faculty'),
        ('College', 'College'),
        ('Suggestion', 'Suggestion'),
        ('Other', 'Other'),
    )

    STUDENT = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    TEACHER = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    complaint_type = models.CharField(
        max_length=50,
        choices=COMPLAINT_TYPES,
        default='Other'
    )

    title = models.CharField(
        max_length=200,
        default="No Title"
    )

    complaint = models.TextField()

    date = models.DateField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=30,
        default="Pending"
    )

    reply = models.TextField(
        default="Not Replied"
    )

    def __str__(self):
        return self.title