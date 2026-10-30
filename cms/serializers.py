from rest_framework import serializers

from .models import (
    FactsStatsSection,
    HeroSlide,
    MainNavItem,
    SiteBranding,
    StatBlock,
    UtilityNavLink,
)


class SiteBrandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBranding
        fields = (
            "logo_image_url",
            "title_line_one",
            "title_line_two",
            "show_search",
            "search_url",
        )


class UtilityNavLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityNavLink
        fields = ("id", "label", "url", "sort_order")


class MainNavItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNavItem
        fields = ("id", "label", "url", "has_dropdown", "sort_order")


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = (
            "id",
            "headline",
            "cta_label",
            "cta_url",
            "media_type",
            "media_url",
            "sort_order",
        )


class StatBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatBlock
        fields = ("id", "value", "description", "color_variant", "sort_order")


class FactsStatsSectionSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField()

    class Meta:
        model = FactsStatsSection
        fields = ("title", "stats")

    def get_stats(self, obj):
        qs = obj.stats.filter(is_active=True).order_by("sort_order", "id")
        return StatBlockSerializer(qs, many=True).data

