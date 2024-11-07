from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()
    profile = models.TextField()
    
    def __str__(self):
        return f"{self.name} {self.surname} "    



class Profile(models.Model):
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    student = models.OneToOneField('university.Student',
                                related_name='Profile',
                                on_delete=models.CASCADE)


    
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"    
    
    
    
    
class Profesor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    
    courses = models.ManyToManyField('university.Course', 
                                      related_name="Profesor")   
    
    def __str__(self):
        return f"{self.name} {self.surname} "    
    
    
    
class Class(models.Model):
    course = models.CharField(max_length=255)
    students = models.TextField()
    
    course = models.ForeignKey('university.Course',
                                    related_name='university_class',
                                    on_delete=models.CASCADE)

    students = models.ManyToManyField('university.Student', 
                                      related_name="classes")
    
    