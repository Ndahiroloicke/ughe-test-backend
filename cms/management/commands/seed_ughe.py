from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings

from cms.models import (
    FactsStatsSection,
    HeroSlide,
    MainNavItem,
    SiteBranding,
    StatBlock,
    UtilityNavLink,
)

User = get_user_model()

# Content aligned with ughe.org and the assessment screenshot (editable in Django Admin).
UGHE_BASE = "https://ughe.org"


class Command(BaseCommand):
    help = "Seed UGHE homepage content and predefined login user."

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username=settings.UGHE_APP_USERNAME)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(settings.UGHE_APP_PASSWORD)
        user.save()
        if created:
            self.stdout.write(f"Created Django user: {settings.UGHE_APP_USERNAME}")

        if SiteBranding.objects.exists():
            self.stdout.write("Homepage content already present; skipping content seed.")
            return

        SiteBranding.objects.create(
            logo_image_url="http://localhost:3000/logoUGHE.png",
            title_line_one="UNIVERSITY OF",
            title_line_two="GLOBAL HEALTH EQUITY",
            show_search=True,
            search_url=f"{UGHE_BASE}/?s=",
        )

        UtilityNavLink.objects.all().delete()
        for order, (label, path) in enumerate(
            [
                ("APPLY", f"{UGHE_BASE}/admissions/"),
                ("GET INVOLVED", f"{UGHE_BASE}/get-involved/"),
                ("MEET THE TEAM", f"{UGHE_BASE}/about-us/meet-the-team/"),
                ("MORE", f"{UGHE_BASE}/"),
            ]
        ):
            UtilityNavLink.objects.create(label=label, url=path, sort_order=order)

        MainNavItem.objects.all().delete()
        nav_items = [
            ("About Us", f"{UGHE_BASE}/about-us/", True),
            ("Academics", f"{UGHE_BASE}/academics/", True),
            ("Research", f"{UGHE_BASE}/research/", True),
            ("Centres and Institutes", f"{UGHE_BASE}/centres-and-institutes/", True),
            ("Admissions", f"{UGHE_BASE}/admissions/", True),
            ("News and Events", f"{UGHE_BASE}/news-and-events/", True),
        ]
        for order, (label, url, dropdown) in enumerate(nav_items):
            MainNavItem.objects.create(
                label=label, url=url, has_dropdown=dropdown, sort_order=order
            )

        HeroSlide.objects.all().delete()
        HeroSlide.objects.create(
            headline=(
                "The Inaugural Paul E. Farmer Butaro Dialogues: Leaders, partners, "
                "students, and health practitioners gathered at UGHE's Butaro Campus "
                "to advance innovation for maternal and newborn health"
            ),
            cta_label="Explore more",
            cta_url=f"{UGHE_BASE}/news-and-events/",
            media_type=HeroSlide.MediaType.IMAGE,
            media_url=(
                "https://ughe.org/wp-content/uploads/2024/06/"
                "Paul-E-Farmer-Butaro-Dialogues-UGHE.jpg"
            ),
            sort_order=0,
        )
        HeroSlide.objects.create(
            headline="University of Global Health Equity — advancing health equity worldwide.",
            cta_label="Explore more",
            cta_url=UGHE_BASE,
            media_type=HeroSlide.MediaType.IMAGE,
            media_url=(
                "https://ughe.org/wp-content/uploads/2023/09/"
                "UGHE-Butaro-Campus-Aerial.jpg"
            ),
            sort_order=1,
        )

        FactsStatsSection.objects.all().delete()
        section = FactsStatsSection.objects.create(title="Facts & Stats", is_active=True)
        stats = [
            ("128", "Trained community members through UGHE entrepreneurship initiatives", "primary"),
            ("1,260", "Community members employed for Campus projects", "secondary"),
            (
                "677",
                "Leaders across 61 countries trained in our Executive Education since 2016",
                "primary",
            ),
            (
                "4TH",
                "Among 129 Universities in Sub-Saharan Africa (Times Higher Education Rankings 2024)",
                "secondary",
            ),
        ]
        for order, (value, description, variant) in enumerate(stats):
            StatBlock.objects.create(
                section=section,
                value=value,
                description=description,
                color_variant=variant,
                sort_order=order,
            )

        self.stdout.write(self.style.SUCCESS("UGHE seed data applied."))
