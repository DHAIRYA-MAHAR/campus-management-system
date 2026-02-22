from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    student_name = models.CharField(max_length=100)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=50)
