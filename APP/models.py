from django.db import models

# College placement management system models

class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=40)
    roll_number = models.CharField(max_length=15)
    email = models.EmailField()
    year=models.CharField(max_length=20)
    phone_number = models.CharField(max_length=13)
    password = models.CharField(max_length=50)
    placed = models.BooleanField(default=False)
    interested = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Drive(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    salary_package = models.IntegerField()
    last_date_of_registration = models.DateField()
    eligibility = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    job_type = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    location = models.CharField(max_length=50)
    batchCanApply=models.CharField(max_length=20)
    
    def __str__(self):
        return self.job_title


class PassedOut(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    salary_package = models.IntegerField()
    last_date_of_registration = models.DateField()
    eligibility = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    job_type = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.student.name} applied for {self.drive.job_title}"
