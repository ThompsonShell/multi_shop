from apps.categories.models import Category


def categories(request):
    return {
        'categories': Category.objects.filter(parent__isnull=True)
    }