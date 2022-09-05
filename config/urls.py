from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from contact_form.views import FeedBackView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Klinika 21 API",
        description="...",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('doctor/', include('doctor.urls')),
    path('docs/', schema_view.with_ui("swagger")),
    path("feedback/", FeedBackView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




