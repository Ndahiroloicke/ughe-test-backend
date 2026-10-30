import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FactsStatsSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="Facts & Stats", max_length=120)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Facts & Stats section",
                "verbose_name_plural": "Facts & Stats sections",
            },
        ),
        migrations.CreateModel(
            name="HeroSlide",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.TextField()),
                ("cta_label", models.CharField(default="Explore more", max_length=80)),
                ("cta_url", models.URLField(default="https://ughe.org", max_length=500)),
                (
                    "media_type",
                    models.CharField(
                        choices=[("image", "Image"), ("video", "Video")],
                        default="image",
                        max_length=10,
                    ),
                ),
                (
                    "media_url",
                    models.URLField(
                        help_text="Public URL to image or video file.", max_length=500
                    ),
                ),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Hero slide",
                "verbose_name_plural": "Hero slides",
                "ordering": ["sort_order", "id"],
            },
        ),
        migrations.CreateModel(
            name="MainNavItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=120)),
                ("url", models.URLField(blank=True, max_length=500)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("has_dropdown", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Main navigation item",
                "verbose_name_plural": "Main navigation items",
                "ordering": ["sort_order", "id"],
            },
        ),
        migrations.CreateModel(
            name="SiteBranding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo_image_url",
                    models.URLField(
                        help_text="URL to UGHE logo image (e.g. from ughe.org media).",
                        max_length=500,
                    ),
                ),
                ("title_line_one", models.CharField(default="UNIVERSITY OF", max_length=120)),
                (
                    "title_line_two",
                    models.CharField(default="GLOBAL HEALTH EQUITY", max_length=120),
                ),
                ("show_search", models.BooleanField(default=True)),
                (
                    "search_url",
                    models.URLField(blank=True, default="https://ughe.org", max_length=500),
                ),
            ],
            options={
                "verbose_name": "Site branding",
                "verbose_name_plural": "Site branding",
            },
        ),
        migrations.CreateModel(
            name="UtilityNavLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=80)),
                ("url", models.URLField(max_length=500)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Utility navigation link",
                "verbose_name_plural": "Utility navigation links",
                "ordering": ["sort_order", "id"],
            },
        ),
        migrations.CreateModel(
            name="StatBlock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        help_text='e.g. "128", "1,260", "4TH"', max_length=32
                    ),
                ),
                ("description", models.TextField()),
                (
                    "color_variant",
                    models.CharField(
                        choices=[
                            ("primary", "Primary red"),
                            ("secondary", "Secondary red"),
                        ],
                        default="primary",
                        max_length=16,
                    ),
                ),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats",
                        to="cms.factsstatssection",
                    ),
                ),
            ],
            options={
                "verbose_name": "Stat block",
                "verbose_name_plural": "Stat blocks",
                "ordering": ["sort_order", "id"],
            },
        ),
    ]
