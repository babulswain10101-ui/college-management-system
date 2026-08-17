from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from students.views import home


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("dashboard/", include("dashboard.urls")),
    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
    path("departments/", include("departments.urls")),
    path("courses/", include("courses.urls")),
    path("attendance/", include("attendance.urls")),
    path("fees/", include("fees.urls")),
    path("results/", include("results.urls")),
    path("accounts/", include("accounts.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )