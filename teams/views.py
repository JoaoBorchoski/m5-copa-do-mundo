from .models import Team
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Response
from .utils import data_processing
from .exceptions import NegativeTitlesError, ImpossibleTitlesError, InvalidYearCupError


class TeamView(APIView):
    def post(self, request):
        try:
            data_processing(request.data)
            team = Team.objects.create(**request.data)
            return Response(model_to_dict(team), 201)
        except NegativeTitlesError:
            return Response({"error": NegativeTitlesError.default_message}, 400)
        except ImpossibleTitlesError:
            return Response({"error": ImpossibleTitlesError.default_message}, 400)
        except InvalidYearCupError:
            return Response({"error": InvalidYearCupError.default_message}, 400)

    def get(self, request):
        teams = Team.objects.all()
        team_dict = [model_to_dict(team) for team in teams]

        return Response(team_dict, 200)


class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            return Response(model_to_dict(team))
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()
            return Response(None, 204)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            for key, value in request.data.items():
                setattr(team, key, value)
            team.save()
            return Response(model_to_dict(team))

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
