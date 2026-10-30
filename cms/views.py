from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

from .models import (
    FactsStatsSection,
    HeroSlide,
    MainNavItem,
    SiteBranding,
    UtilityNavLink,
)
from .serializers import (
    FactsStatsSectionSerializer,
    HeroSlideSerializer,
    MainNavItemSerializer,
    SiteBrandingSerializer,
    UtilityNavLinkSerializer,
)

User = get_user_model()


class HomepageView(APIView):
    """Public homepage payload for Next.js."""

    def get(self, request):
        branding = SiteBranding.objects.first()
        if not branding:
            return Response(
                {"detail": "No site branding configured. Run seed_ughe or add content in admin."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        facts = FactsStatsSection.objects.filter(is_active=True).first()

        facts_data = (
            FactsStatsSectionSerializer(facts).data if facts else None
        )
        return Response(
            {
                "branding": SiteBrandingSerializer(branding).data,
                "utility_links": UtilityNavLinkSerializer(
                    UtilityNavLink.objects.filter(is_active=True), many=True
                ).data,
                "main_nav": MainNavItemSerializer(
                    MainNavItem.objects.filter(is_active=True), many=True
                ).data,
                "hero_slides": HeroSlideSerializer(
                    HeroSlide.objects.filter(is_active=True), many=True
                ).data,
                "facts_stats": facts_data,
            }
        )


class LoginView(APIView):
    """
    Login with predefined credentials (see readme.txt / Docker env).
    Returns JWT access and refresh tokens.
    """

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        expected_user = settings.UGHE_APP_USERNAME
        expected_pass = settings.UGHE_APP_PASSWORD

        if username != expected_user or password != expected_pass:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user, _ = User.objects.get_or_create(
            username=expected_user,
            defaults={"is_staff": True, "is_superuser": True},
        )
        if not user.check_password(expected_pass):
            user.set_password(expected_pass)
            user.is_staff = True
            user.is_superuser = True
            user.save()

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username,
            }
        )


class MeView(APIView):
    """Simple authenticated check for the Next.js login flow."""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user or not request.user.is_authenticated:
            return Response({"authenticated": False}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(
            {
                "authenticated": True,
                "username": request.user.username,
            }
        )
