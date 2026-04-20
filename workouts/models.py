from django.db import models


class Workout(models.Model):
    title = models.CharField(max_length=200)
    duration_min = models.IntegerField(default=30)
    completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    repetitions = models.IntegerField(default=1)
    sets = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.workout.title})"
