from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
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
                raise ValidationError('you can creat only three category')
        except AttributeError:
            pass

    # def category_filter(self):
    #     if self.parent is None:
    #         return self.name
    #     elif self.parent.parent is not None and self.children:
    #         return self.name
    #     elif self.parent.parent is not None and self.children is None:
    #         return self.name

    def __str__(self):
        return self.name
