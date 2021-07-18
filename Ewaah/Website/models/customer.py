from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

        

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
