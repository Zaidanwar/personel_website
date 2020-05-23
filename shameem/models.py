from django.db import models

# Create your models here.
class Personal_detail(models.Model):
    heading = models.CharField(max_length=30, default="")
    description=models.CharField(max_length=75, default="")
    def __str__(self):
        return self.heading

class Description(models.Model):
    no=models.IntegerField(default=0)
    title=models.CharField(max_length=20, default="")
    description = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.title


class Project(models.Model):
    no=models.IntegerField(default=0)
    title = models.CharField(max_length=40, default="")
    description=models.CharField(max_length=300,default='')
    document=models.FileField(upload_to='reports/')
    def __str__(self):
        return (str(self.no) + " - " + str(self.title))



class Profile_photo(models.Model):
    description = models.CharField(max_length=20, default="")
    image=models.ImageField(upload_to='dp/')
    def __str__(self):
        return self.description
class Language_skill(models.Model):
    no = models.IntegerField(default=0)
    language = models.CharField(max_length=20, default="")
    knowledge_in_percentage=models.IntegerField(default=0)
    def __str__(self):
        return (str(self.no) + " - " + str(self.language))


class Education(models.Model):
    no=models.IntegerField(default=0)
    course = models.CharField(max_length=100, default="")
    institution=models.CharField(max_length=300,default='')
    academic_year=models.CharField(max_length=20, default="")
    website=models.CharField(max_length=100, default="",)
    institution_image=models.ImageField(upload_to='dp/')
    university_name=models.CharField(max_length=300,default='')
    university_website = models.CharField(max_length=300, default='')
    university_logo=models.ImageField(upload_to='dp/')

    def __str__(self):
        return (str(self.no) + " - " + str(self.course))

class Hobbie(models.Model):
    no=models.IntegerField(default=0)
    hobby = models.CharField(max_length=50, default="")
    description=models.CharField(max_length=500,default='')
    image=models.ImageField(upload_to='dp/')

    def __str__(self):
        return (str(self.no) + " - " + str(self.hobby))



