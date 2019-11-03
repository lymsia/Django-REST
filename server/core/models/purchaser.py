from django.db import models


class Purchaser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchaser'

    def __str__(self):
        return 'Purchaser({}, {}, {})'.format(self.id, self.name, self.created_date)

