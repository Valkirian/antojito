from django.db import models
from django.urls import reverse
from django.contrib.auth.hashers import make_password
# Create your models here.


class ArepadeHuevo(models.Model):
    # Choices
    FTMN = models.TextChoices(
        'Tamano Comida', 'Pequeno Mediano Grande')
    DSPNL = models.TextChoices('Disponibilidad', 'Si No')

    Id = models.AutoField(primary_key=True)
    name = models.CharField(default="Arepa de Huevo", max_length=20)
    Imagen = models.ImageField(upload_to='shop/media', blank=False, null=True)
    Tamano = models.CharField(
        max_length=10, choices=FTMN.choices, blank=False, null=True)
    PrecioU = models.CharField(
        max_length=5, blank=False, null=True)
    Disponible = models.CharField(
        max_length=5, choices=DSPNL.choices, blank=False, null=True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("ArepadeHuevo")
        verbose_name_plural = ("ArepadeHuevos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ArepadeHuevo_detail", kwargs={"pk": self.pk})


class Carimanola(models.Model):

    # Choices
    FTMN = models.TextChoices(
        'Tamano Comida', 'Pequeno Mediano Grande')
    DSPNL = models.TextChoices('Disponibilidad', 'Si No')

    Id = models.AutoField(primary_key=True)
    name = models.CharField(default="Carimanola", max_length=20)
    Imagen = models.ImageField(upload_to='shop/media', blank=False, null=True)
    Tamano = models.CharField(
        max_length=10, choices=FTMN.choices, blank=False, null=True)
    PrecioU = models.CharField(
        max_length=5, blank=False, null=True)
    Disponible = models.CharField(
        max_length=5, choices=DSPNL.choices, blank=False, null=True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Carimanola")
        verbose_name_plural = ("Carimanolas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Carimanola_detail", kwargs={"pk": self.pk})


class Empanada(models.Model):

    # Choices
    FTMN = models.TextChoices(
        'Tamano Comida', 'Pequeno Mediano Grande')
    DSPNL = models.TextChoices('Disponibilidad', 'Si No')

    Id = models.AutoField(primary_key=True)
    name = models.CharField(default="Empanada", max_length=20)
    Imagen = models.ImageField(upload_to='shop/media', blank=False, null=True)
    Tamano = models.CharField(
        max_length=10, choices=FTMN.choices, blank=False, null=True)
    PrecioU = models.CharField(
        max_length=5, blank=False, null=True)
    Disponible = models.CharField(
        max_length=5, choices=DSPNL.choices, blank=False, null=True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Empanada")
        verbose_name_plural = ("Empanadas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Empanada_detail", kwargs={"pk": self.pk})


class Salchipapa(models.Model):

    # Choices
    FTMN = models.TextChoices(
        'Tamano Comida', 'Pequeno Mediano Grande')
    DSPNL = models.TextChoices('Disponibilidad', 'Si No')

    Id = models.AutoField(primary_key=True)
    name = models.CharField(default="Salchipapa", max_length=20)
    Imagen = models.ImageField(upload_to='shop/media', blank=False, null=True)
    Tamano = models.CharField(
        max_length=10, choices=FTMN.choices, blank=False, null=True)
    PrecioU = models.CharField(
        max_length=5, blank=False, null=True)
    Disponible = models.CharField(
        max_length=5, choices=DSPNL.choices, blank=False, null=True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Salchipapa")
        verbose_name_plural = ("Salchipapas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Salchipapa_detail", kwargs={"pk": self.pk})


class Bollo(models.Model):

    # Choices
    FTMN = models.TextChoices(
        'Tamano Comida', 'Pequeno Mediano Grande')
    DSPNL = models.TextChoices('Disponibilidad', 'Si No')

    Id = models.AutoField(primary_key=True)
    name = models.CharField(default="Bollo", max_length=20)
    Imagen = models.ImageField(upload_to='shop/media', blank=False, null=True)
    Tamano = models.CharField(
        max_length=10, choices=FTMN.choices, blank=False, null=True)
    PrecioU = models.CharField(
        max_length=5, blank=False, null=True)
    Disponible = models.CharField(
        max_length=5, choices=DSPNL.choices, blank=False, null=True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Bollo")
        verbose_name_plural = ("Bollos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bollo_detail", kwargs={"pk": self.pk})
