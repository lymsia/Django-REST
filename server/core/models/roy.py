from django.db import models


class Roy(models.Model):

    id = models.AutoField(primary_key=True)
    add = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'roy'

    def __str__(self):
        return '{}'.format(self.name)

