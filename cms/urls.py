from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)
from graphene_django.views import GraphQLView
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from cms.schema import schema
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True,
                                                schema=schema))),

    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    path('', include(router.urls)),
    path('api/businesses/', include('businesses.urls')),
]
