from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class AssignUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time field for storing the creation time
    updated_at = models.DateTimeField(auto_now=True)  #

    def __str__(self):
        return self.name


class CorrectiveAction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time field for storing the creation time
    updated_at = models.DateTimeField(auto_now=True)  #

    def __str__(self):
        return self.name


class HaccpAdminData(models.Model):
    id = models.AutoField(primary_key=True)
    storage_location = models.CharField(max_length=200)
    sub_storage_location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    used_for = models.CharField(max_length=200)
    assign_task_to = models.CharField(max_length=200)
    repeat_every = models.IntegerField()
    repeat_frequency = models.CharField(max_length=200)
    time_on = models.JSONField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    corrective_action = models.ManyToManyField(CorrectiveAction)
    assign_verifier = models.ManyToManyField(AssignUsers)
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time field for storing the creation time
    updated_at = models.DateTimeField(auto_now=True)  #

    def __str__(self):
        return self.name[:50]  # Display the first 50 characters of the name field