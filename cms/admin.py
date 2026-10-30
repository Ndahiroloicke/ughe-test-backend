from django.contrib import admin

from .models import (
    FactsStatsSection,
    HeroSlide,
    MainNavItem,
    SiteBranding,
    StatBlock,
    UtilityNavLink,
)


class StatBlockInline(admin.TabularInline):
    model = StatBlock
    extra = 1


@admin.register(SiteBranding)
class SiteBrandingAdmin(admin.ModelAdmin):
    list_display = ("title_line_one", "title_line_two", "show_search")


@admin.register(UtilityNavLink)
class UtilityNavLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")


@admin.register(MainNavItem)
class MainNavItemAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "has_dropdown", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active", "has_dropdown")


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("headline", "media_type", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    list_filter = ("media_type", "is_active")


@admin.register(FactsStatsSection)
class FactsStatsSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    inlines = [StatBlockInline]


@admin.register(StatBlock)
class StatBlockAdmin(admin.ModelAdmin):
    list_display = ("value", "section", "color_variant", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    list_filter = ("section", "color_variant")
