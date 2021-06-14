from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from candidateFinder.Services.MatcherService import MatcherService

@csrf_exempt # for anonymous calls
def candidateFinder(request):
    print(type(request))
    print('in candidateFinder request')
    matcherService = MatcherService()

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    res = matcherService.candidate_finder(body)
    return JsonResponse(res, status=200, safe=False)
