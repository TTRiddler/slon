from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from landing.models import TitleTag, MailToString, MailFromString, Agreement, AboutUs, OurPros


admin.site.register(TitleTag)
admin.site.register(MailToString)
admin.site.register(MailFromString)
admin.site.register(OurPros)
admin.site.register(AboutUs)

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'text')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('seo_title', 'desc', 'keywords'),
        }),
    )


admin.site.unregister(FlatPage)

@admin.register(FlatPage)
class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE())
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)