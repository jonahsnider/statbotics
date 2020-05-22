from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .serializers import (
    TeamMatchSerializer,
    TeamEventSerializer,
    TeamYearSerializer,
    TeamSerializer,
    EventSerializer,
    YearSerializer,
    UserSerializer,
)

from .filters import (
    TeamMatchFilterSet,
    TeamEventFilterSet,
    TeamYearFilterSet,
    TeamFilterSet,
    EventFilterSet,
    YearFilterSet,
)
from .models import (
    TeamMatch,
    TeamEvent,
    TeamYear,
    Team,
    Event,
    Year,
)

from django.contrib.auth.models import User
from django.views.generic.base import RedirectView

class TeamMatchView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TeamMatchSerializer
    queryset = TeamMatch.objects.all()
    filterset_class = TeamMatchFilterSet

class TeamEventView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TeamEventSerializer
    queryset = TeamEvent.objects.all()
    filterset_class = TeamEventFilterSet

class TeamYearView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TeamYearSerializer
    queryset = TeamYear.objects.all()
    filterset_class = TeamYearFilterSet

class TeamView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    filterset_class = TeamFilterSet

class EventView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_class = EventFilterSet

class YearView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = YearSerializer
    queryset = Year.objects.all()
    filterset_class = YearFilterSet

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

'''API SECTION'''
#syntax: '/api/teams/?team=%(num)s&limit=2000&o=time'

class Team(RedirectView):
    url = '/api/_teams/?team=%(num)s'

class Team_Years(RedirectView):
    url = '/api/_team_years/?team=%(num)s&limit=100&o=year'

class Team_Events(RedirectView):
    url = '/api/_team_events/?team=%(num)s&limit=1000&o=time'

class Team_Matches(RedirectView):
    url = '/api/_team_matches/?team=%(num)s&limit=10000&o=time'

class TeamYear(RedirectView):
    url = '/api/_team_years/?team=%(num)s&year=%(year)s'

class TeamYear_Events(RedirectView):
    url = '/api/_team_events/?team=%(num)s&year=%(year)s&limit=100&o=time'

class TeamYear_Matches(RedirectView):
    url = '/api/_team_matches/?team=%(num)s&year=%(year)s&limit=1000&o=time'

class TeamYearEvent(RedirectView):
    url = '/api/_team_events/?team=%(num)s&year=%(year)s&event=%(event)s'

class TeamYearEvent_Matches(RedirectView):
    url = '/api/_team_matches/?team=%(num)s&year=%(year)s&event=%(event)s&limit=100o=time'

class Teams(RedirectView):
    url = '/api/_teams/?limit=10000'

class Teams_byElo(RedirectView):
    url = '/api/_teams/?limit=10000&o=-%(elo)s'

class TeamsActive(RedirectView):
    url = '/api/_teams/?active=1&limit=10000'

class TeamsActive_byElo(RedirectView):
    url = '/api/_teams/?active=1&limit=10000&o=-%(elo)s'

class TeamsDistrict(RedirectView):
    url = '/api/_teams?district=%(district)s&limit=10000'

class TeamDistrict_byElo(RedirectView):
    url = '/api/_teams?district=%(district)s&limit=10000&o=-%(elo)s'

class TeamsDistrictActive(RedirectView):
    url = '/api/_teams?district=%(district)s&active=1&limit=10000'

class TeamsDistrictActive_byElo(RedirectView):
    url = '/api/_teams?district=%(district)s&active=1&limit=10000&o=-%(elo)s'

class TeamsRegion(RedirectView):
    url = '/api/_teams?region=%(region)s&limit=10000'

class TeamsRegion_byElo(RedirectView):
    url = '/api/_teams?region=%(region)s&limit=10000&o=-%(elo)s'

class TeamsRegionActive(RedirectView):
    url = '/api/_teams?region=%(region)s&active=1&limit=10000'

class TeamsRegionActive_byElo(RedirectView):
    url = '/api/_teams?region=%(region)s&active=1&limit=10000&o=-%(elo)s'

class TeamsYear(RedirectView):
    url = '/api/_team_years/?year=%(year)s&limit=10000'

class TeamsYear_byElo(RedirectView):
    url = '/api/_team_years/?year=%(year)s&limit=10000&o=-%(elo)s'

class TeamsYearDistrict(RedirectView):
    url = '/api/_team_years/?year=%(year)s&district=%(district)s&limit=10000'

class TeamsYearDistrict_byElo(RedirectView):
    url = '/api/_team_years/?year=%(year)s&district=%(district)s&limit=10000&o=-%(elo)s'

class TeamsYearRegion(RedirectView):
    url = '/api/_team_years/?year=%(year)s&region=%(region)s&limit=10000'

class TeamsYearRegion_byElo(RedirectView):
    url = '/api/_team_years/?year=%(year)s&region=%(region)s&limit=10000&o=-%(elo)s'

class Year(RedirectView):
    url = '/api/_years/?year=%(year)s'

class YearEvent(RedirectView):
    url = '/api/_events/?year=%(year)s&event=%(event)s'

class Years(RedirectView):
    url = '/api/_years/?limit=100'

class Events(RedirectView):
    url = '/api/_events/?limit=10000'

class Events_byElo(RedirectView):
    url = '/api/_events/?limit=10000&o=-%(elo)s'

class EventYear(RedirectView):
    url = '/api/_events/?year=%(year)s&limit=1000'

class EventYear_byElo(RedirectView):
    url = '/api/_events/?year=%(year)s&limit=1000&o=-%(elo)s'
