from django.http import JsonResponse
from djangoApiDec.djangoApiDec import queryString_required

# Create your views here.
@queryString_required(['fft'])
def bayes(request):
	from sklearn import svm
	fft = request.GET['fft']
	fft = fft.split()
	X = [[0, 0], [2, 2]]
	y = [0.5, 2.5]
	clf = svm.SVR()
	clf.fit(X, y) 
	return JsonResponse(list(clf.predict([fft])), safe=False)