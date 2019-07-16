from django.contrib import admin
from services.models import *


class ImageInServiceInline(admin.TabularInline):
    model = ImageInService
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ImageInServiceInline]
    fieldsets = (
        (None, {
            'fields': ('categories', 'specialists', 'title', 'schedule', 'one_lesson_price', 'some_lesson_nmb', 'some_lesson_price', 'text', 'is_active')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    filter_horizontal = ('categories', 'specialists')
    prepopulated_fields = {'slug': ('title',)}


class ImageInArtclassInline(admin.TabularInline):
    model = ImageInArtclass
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title1', 'title2', 'color_prefix')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    prepopulated_fields = {'slug': ('title1', 'title2')}


@admin.register(Artclass)
class ArtclassAdmin(admin.ModelAdmin):
    inlines = [ImageInArtclassInline]
    fieldsets = (
        (None, {
            'fields': ('categories', 'specialists', 'title', 'schedule', 'one_lesson_price', 'some_lesson_nmb', 'some_lesson_price', 'text', 'is_active')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    filter_horizontal = ('categories', 'specialists')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name',)


class WeekDayServiceElemInline(admin.TabularInline):
    model = WeekDayServiceElem
    extra = 0


class WeekDayArtclassElemInline(admin.TabularInline):
    model = WeekDayArtclassElem
    extra = 0


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    inlines = [WeekDayArtclassElemInline, WeekDayServiceElemInline]
    list_display = ('name', 'short_name', 'slug_name')
    prepopulated_fields = {'slug_name': ('short_name',)}

    
