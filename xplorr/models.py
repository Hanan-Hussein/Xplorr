from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Country(models.Model):
    """
    country
    """
    name = models.CharField(max_length=100)
    iso = models.CharField(max_length=50)
    code = models.IntegerField()

    @classmethod
    def __str__(self):
        return f"country:{self.name}: iso: {self.iso}: code:{self.code}"

    @classmethod
    def save_country(cls, country):
        cls.save(country)


class City(models.Model):
    """
    city
    """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @classmethod
    def __str__(self):
        return f"city:{self.name}: country:{self.country}"

    @classmethod
    def save_city(cls, city):
        cls.save(city)


class Goals(models.Model):
    """
    goals that are tied to a user or group of users
    """
    goalName = models.CharField(max_length=100)
    moneySaved = models.IntegerField()
    image = CloudinaryField("image", blank=True, null=True)
    user = models.ForeignKey(
        User, related_name="users_goal", on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

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


class Profile(models.Model):
    """
    user's profile
    """
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    # goals = models.ForeignKey(Goals, related_name="goals", on_delete=models.CASCADE, null=True)
    profile_image = CloudinaryField("profile", blank=True, null=True)

    @classmethod
    def __str__(self):
        return f"user:{self.user}: course:{self.goals}"

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)

class Category(models.Model):
    """
    category
    """
    name = models.CharField(max_length=100)
    category_image = CloudinaryField("category_image", blank=True, null=True)


class Accomodation(models.Model):
    """
    Accomodation
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    price = models.IntegerField()

    @classmethod
    def __str__(self):
        return f"Accomodation:{self:name}: location:{self.location}: city:{self.city}: price:{self.price}: category:{self.category}"

    @classmethod
    def save_accomodation(cls, accomodation):
        cls.save(accomodation)


class Sightseeing(models.Model):
    """
    Sightseeing in a city
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    @classmethod
    def __str__(self):
        return f"Sight:{self.name}: location:{self.location}: city:{self.city}: price:{self.price}: category:{self.category}"

    @classmethod
    def save_sightseeing(cls, sightseeing):
        cls.save(sightseeing)
