from django.db import models

class Car(models.Model):
    year = models.IntegerField(max_length=4)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self) -> str:
        return (
            f"==Year==: {self.year}\n"
            f"==Make==: {self.make}\n"
            f"==Model==: {self.model}\n"
            f"==Color==: {self.color}\n"   
        )
