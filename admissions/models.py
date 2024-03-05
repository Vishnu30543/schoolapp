from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    fathername= models.CharField(max_length=100)
    classname= models.IntegerField()
    contact= models.CharField(max_length=10)


from django.urls import reverse
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    exp = models.IntegerField()
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    # Create
    def get_absolute_url(self):
        # we can't assign url directly , first keep a name in url and use it
        # In reverse function we can't use url so we use name
        # for crud operations give name for urls
        return reverse('listteachers')
#return reverse('teacherdetails', kwargs= {'pk':self.pk})


