from multiprocessing.process import parent_process

from apps.categories.models import Category


def categories(request, *args, **kwargs):
    return {
        'categories': Category.objects.filter(parent__isnull=True)
    }
