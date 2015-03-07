from django.shortcuts import render
from .models import Twitter

# Create your views here.
def twitter_list(request):
    try:
        req_arg = request.GET['id']
        print req_arg
    except:
        req_arg = 'java'

    tweets = Twitter.objects.filter(tweets__icontains=req_arg)
    print tweets
    return render(request, 'templates/home.html', {'tweets': tweets})




