from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rankings.serializers import YearSerializer
from rankings.models import Year as YearModel
