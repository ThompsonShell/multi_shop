from django.db import models


class Category(models.Model):
    # <<<<<<<<<< this model create category >>>>>>>>>>


    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(to='self',
                               null=True,
                               blank=True,
                               related_name='children',
                               on_delete=models.CASCADE,
                               related_query_name='category'
                               )


    def clean(self):
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValueError({'parent': 'only add 3'})
        except AttributeError:
            pass


    def __str__(self):
        return self.name
