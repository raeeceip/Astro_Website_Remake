from django.db import models

# Create your models here.

class Experience(models.Model):
    company = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    designation = models.CharField(max_length=30)
    public = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.company}"


class ExperienceSAR(models.Model):
    statement = models.TextField()
    index = models.IntegerField()
    experience = models.ForeignKey(Experience, related_name='experience_sars', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['index', 'experience']
        ordering = ['experience', 'index']

    def __str__(self) -> str:
        return f"{self.experience} {self.index}"


class Article(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    icon = models.CharField(max_length=50)
    data = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.contact_name