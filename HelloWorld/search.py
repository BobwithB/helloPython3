from django.http import HttpResponse
from django.shortcuts import render_to_response

def get(request):
    return render_to_response('get.html')
def post(request):
    return render_to_response('post.html')

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'ur search msg: ' + request.GET['q']
    else:
        message = 'the msg u submit is empty...'
    print('msg = '+message)
    return HttpResponse(message)