from django.db import models


class SiteBranding(models.Model):
    """Logo and site title shown in the header (single row in admin)."""

    logo_image_url = models.URLField(
        max_length=500,
        help_text="URL to UGHE logo image (e.g. from ughe.org media).",
    )
    title_line_one = models.CharField(max_length=120, default="UNIVERSITY OF")
    title_line_two = models.CharField(max_length=120, default="GLOBAL HEALTH EQUITY")
    show_search = models.BooleanField(default=True)
    search_url = models.URLField(max_length=500, default="https://ughe.org", blank=True)

    class Meta:
        verbose_name = "Site branding"
        verbose_name_plural = "Site branding"

    def __str__(self):
        return "Site branding"


class UtilityNavLink(models.Model):
    label = models.CharField(max_length=80)
    url = models.URLField(max_length=500)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Utility navigation link"
        verbose_name_plural = "Utility navigation links"

    def __str__(self):
        return self.label


class MainNavItem(models.Model):
    label = models.CharField(max_length=120)
    url = models.URLField(max_length=500, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    has_dropdown = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Main navigation item"
        verbose_name_plural = "Main navigation items"

    def __str__(self):
        return self.label


class HeroSlide(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "image", "Image"
        VIDEO = "video", "Video"

    headline = models.TextField()
    cta_label = models.CharField(max_length=80, default="Explore more")
    cta_url = models.URLField(max_length=500, default="https://ughe.org")
    media_type = models.CharField(
        max_length=10, choices=MediaType.choices, default=MediaType.IMAGE
    )
    media_url = models.URLField(
        max_length=500,
        help_text="Public URL to image or video file.",
    )
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Hero slide"
        verbose_name_plural = "Hero slides"

    def __str__(self):
        return self.headline[:60] + ("…" if len(self.headline) > 60 else "")


class FactsStatsSection(models.Model):
    """Section heading for Facts & Stats (typically one active row)."""

    title = models.CharField(max_length=120, default="Facts & Stats")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Facts & Stats section"
        verbose_name_plural = "Facts & Stats sections"

    def __str__(self):
        return self.title


class StatBlock(models.Model):
    class ColorVariant(models.TextChoices):
        PRIMARY = "primary", "Primary red"
        SECONDARY = "secondary", "Secondary red"

    section = models.ForeignKey(
        FactsStatsSection,
        related_name="stats",
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=32, help_text='e.g. "128", "1,260", "4TH"')
    description = models.TextField()
    color_variant = models.CharField(
        max_length=16,
        choices=ColorVariant.choices,
        default=ColorVariant.PRIMARY,
    )
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Stat block"
        verbose_name_plural = "Stat blocks"

    def __str__(self):
        return f"{self.value} — {self.description[:40]}"
