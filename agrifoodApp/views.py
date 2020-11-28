from django.shortcuts import render

# Create your views here.
def index(request) :
    # context = {'ment' : '여기까지 잘되시나요?'}
    return render(request, 'index.html')