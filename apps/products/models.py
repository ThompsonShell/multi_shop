from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.categories.models import Category
from apps.comments.models import ProductComment
from apps.general.models import General
from apps.ratings.models import ProductRating


class Product(models.Model):
    """ this model create new product   
    
           For example:
    
           <<<<<<<<<<{'name':'laptop', 'category':'technique', 'price':'10000', 'currency':'USD'}>>>>>>>>>>>
    
    """
    title = models.CharField(max_length=150)
    avg_rating = models.DecimalField(max_digits=10, decimal_places=1, default=Decimal('0'), editable=False)
    comments_count = models.DecimalField(max_digits=10, decimal_places=0, default=Decimal('0'), editable=False)
    currency = models.CharField(max_length=5, choices=General.Currency.choices, default='UZS')
    short_description = models.CharField(max_length=250)
    long_description = models.TextField(max_length=10_000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to='products/images/%Y/%m/%d/')
    old_price = models.DecimalField(max_digits=10, decimal_places=1, default=Decimal('0'), editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=1, default=Decimal('0'), editable=False)

    def get_features(self):
        print(1111)
        product_features = ProductFeatures.objects.prefetch_related('feature_values').filter(product_id=self.pk)
        features = {}
        for product_feature in product_features:
            for value in product_feature.feature_values.all():
                if value.feature_id not in features:
                    features[value.feature_id] = {
                        'id': value.feature_id,
                        'name': value.feature.name,
                        'values': [
                            {'id': value.id, 'value': value.name}
                        ],
                    }
                else:
                    features[value.feature_id]['values'].append(
                        {'id': value.id, 'name': value.name}
                    )
            return list(features.values())

    def set_avg_rating(self):
        aggregated_amount = ProductRating.objects.filter(
            product_id=self.pk
        ).aggregate(
            avg=models.Avg('rating', default=0),
        )
        self.avg_rating = round(aggregated_amount['avg'], 1)
        self.save()


    def save(self, *args, **kwargs):
        self.comments_count = ProductComment.objects.filter(product_id=self.pk).count()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    class ProductImage(models.Model):
        """ this model upload to image for product """

        product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
        image = models.ImageField(upload_to='product/images/%Y/%m/%d/')
        ordering_number = models.PositiveSmallIntegerField(default=0)



class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_value = models.ManyToManyField('features.FeatureValue')
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(max_digits=20, decimal_places=2)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.product.old_price,  self.product.price = self.old_price, self.price
        self.product.save()