import graphene
from graphene_django import DjangoObjectType
from django_filters import OrderingFilter
from .models import Business
import math
from decimal import Decimal


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business


class Query(graphene.ObjectType):
    businesses_nearby = graphene.List(
        BusinessType,
        latitude=graphene.Float(required=True),
        longitude=graphene.Float(required=True)
    )

    def resolve_businesses_nearby(self, info, latitude, longitude, distance_limit=10):
        def get_distance_from_lat_lon_in_miles(lat1, lon1, lat2, lon2):
            earth_radius = 3958.8  # Earth radius in miles

            lat1 = Decimal(lat1)
            lon1 = Decimal(lon1)
            lat2 = Decimal(lat2)
            lon2 = Decimal(lon2)
            pi = Decimal(math.pi)

            delta_lat = (lat2 - lat1) * pi / 180
            delta_lon = (lon2 - lon1) * pi / 180
            a = (math.sin(delta_lat / 2) * math.sin(delta_lat / 2) +
                 math.cos(lat1 * pi / 180) * math.cos(lat2 * pi / 180) *
                 math.sin(delta_lon / 2) * math.sin(delta_lon / 2))
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = earth_radius * c
            return distance

        nearby_businesses = []
        for business in Business.objects.all():
            distance = get_distance_from_lat_lon_in_miles(latitude, longitude, business.latitude, business.longitude)
            if distance <= distance_limit:
                nearby_businesses.append(business)

        return nearby_businesses


schema = graphene.Schema(query=Query)
