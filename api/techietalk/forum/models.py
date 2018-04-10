from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Forum(models.Model):
    problem = models.CharField(max_length=255)
    statement = models.CharField(max_length=20000)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"

    def __str__(self):
        return self.problem