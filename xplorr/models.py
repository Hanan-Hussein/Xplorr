from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Goals(models.Model):
    """
    goals that are tied to a user or group of users
    """
    goalName = models.CharField(max_length=100)
    moneySaved = models.IntegerField()
    image = CloudinaryField("image", blank=True, null=True)
    user = models.ForeignKey(
        User, related_name="users_goal", on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.goalName}: moneySaved:{self.moneySaved}: image:{self.image}: user:{self.user}"

    @classmethod
    def save_goals(self, goals):
        """
        saves goals
        """
        self.save(goals)

    @classmethod
    def delete_goal(self, goal):
        """
        deletes goals
        """
        self.delete(goal)

    @classmethod
    def update_goal(self, goal):
        """
        updates goals
        """
        self.update(goalName=goal)


