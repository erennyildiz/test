from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=300)

class Account(models.Model):
    money_on_account = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Transfer(models.Model):
    amount = models.IntegerField()
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_account')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='from_account')
    from_account_new_amount = models.IntegerField(null=True , blank=True)
    to_account_new_amount = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.from_account.money_on_account = self.from_account.money_on_account - self.amount
        self.from_account.save()
        self.from_account_new_amount = self.from_account.money_on_account 
        self.to_account.money_on_account = self.to_account.money_on_account + self.amount
        self.to_account.save()
        self.to_account_new_amount = self.to_account.money_on_account 
        super(Transfer, self).save(*args, **kwargs)

