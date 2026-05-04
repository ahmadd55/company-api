from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    Company_type=models.CharField(max_length=50,choices=(('IT','IT'),('CORPORATE','Corperate'),('STARTUP', 'Startup'),
                                                        ('SME', 'Small/Medium Enterprise')))
    created=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company=models.ForeignKey("Company",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    Salary=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address=models.CharField(max_length=50)
    joining=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
                                                                    
                                                                
