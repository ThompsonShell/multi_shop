from multiprocessing.process import parent_process
from django.contrib.admin import SimpleListFilter

from apps.categories.context_processors import categories


class CategoryFilter(SimpleListFilter):
    title = 'Category degree'
    parameter_name = 'category'


    def lookups(self, request, model_admin):
        return [
            ('main_cat', 'Main category'),
            ('middle_cat', 'Middle category'),
            ('low_cat', 'Low category'),
        ]

    def queryset(self, request, queryset):
        match self.value():
            case 'main_cat':
                return queryset.filter(parent__isnull=True)
            case 'middle_cat':
                return queryset.filter(parent__isnull=False, category__isnull=False)
            case 'low_cat':
                return queryset.filter(parent__parent__isnull=False)