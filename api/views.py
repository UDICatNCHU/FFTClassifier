from django.http import JsonResponse#to make the web exe
# Create your views here.
def krunt(request):
	return JsonResponse([1, 2, 3], safe=False)#JsonResponse(the output you want to show),if safe=True->can't use array
