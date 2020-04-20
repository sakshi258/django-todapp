from django.db import models
from django.shortcuts import reverse
from datetime import datetime as dt
import datetime

# Create your models here.


Choices = ("All", "Grocery", "Personal", "Work")

TAG_CHOICES = ["Overdue", "Today", "Tomorrow", "Long Term"]


class TodoItem(models.Model):
    todoitem = models.CharField(default = "Todo task", max_length = 50)
    note = models.CharField(blank = True, null = True, max_length = 50)
    completed = models.BooleanField(default = False)
    due_date = models.DateField(default = datetime.date.today)

    @property
    def get_tag(self):
        due_date = self.due_date
        today = datetime.date.today()
        timedelta = datetime.timedelta(days = 1)
        yesterday = today - timedelta
        tomorrow = today + timedelta
        if due_date == today:
            return TAG_CHOICES[1]
        elif due_date == yesterday:
            return TAG_CHOICES[0]
        elif due_date == tomorrow:
            return TAG_CHOICES[2]
        elif due_date > tomorrow:
            return TAG_CHOICES[3]

    def __str__(self):
        return f"{self.todoitem}"

    def get_absolute_url(self):
        return reverse('todoapp:home-url')
