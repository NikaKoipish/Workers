from django.db import models

NULLABLE = {"null": True, "blank": True}


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    brigade_number = models.IntegerField(verbose_name="Номер бригады")
    salary = models.IntegerField(verbose_name="Зарплата")
    specialization = models.CharField(max_length=50, verbose_name="Специализация")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
