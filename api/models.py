from django.db import models


class Artest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['id']


class Alobom(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artest, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Songs(models.Model):
    title = models.CharField(max_length=50)
    alobom = models.ForeignKey(Alobom, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Bastakora(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        ordering = ['id']


