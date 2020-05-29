from django.db import models


TYPE_CHOICES = {
    ('Withdrawal','Withdrawal'),
    ('Deposit','Deposit'),

}

# Create your models here.

class Account(models.Model):
    firstName = models.CharField(max_length=60, default="", blank=True, null=False)
    lastName = models.CharField(max_length=60, default="", blank=True, null=False)
    startingBalance = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    accounts = models.Manager()

    def __str__(self):
        return "Name: {} {} Account: {}".format(self.firstName,self.lastName,self.id)

class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, null=False)
    amount = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE, null=False)

    transactions = models.Manager()

    def __str__(self):
        return "Number: {} Date: {} Type: {} Amount: {}".format(str(self.id),str(self.date),self.type,str(self.amount))