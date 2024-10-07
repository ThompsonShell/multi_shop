from modeltranslation.admin import TranslationAdmin

from apps.abouts.models import About
from django.contrib import admin


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    group_fieldsets = True

    # def has_add_permission(self, request):
    #     return not About.objects.exists()
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

        # def has_view_permission(self, request, obj=None):
        #     return False
    #
    #
    # def get_queryset(self, request):
    #     return About.objects.all()
    # def has_view_or_change_permission(self, request, obj=None):
    #     return True


    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }
