from django.shortcuts import render
from django.http import HttpResponse
from .models import ViewCount,overallView
from django.db.models import F

# Create your views here.
def show_surprise(request,user_id,surprise_id):

    try:
        user = ViewCount.objects.get(user_id=user_id,surprise_id=surprise_id,count=1)
        print('user ',user)


    except:
        print('entered in except')
        entry = ViewCount.objects.create(user_id=user_id,surprise_id=surprise_id,count=1)
        entry.save()
        overallView.objects.filter(pk=1).update(all_count=F('all_count') + 1)

    finally:
        viewcount=overallView.objects.get(pk=1)
        if viewcount.all_count in [3,4,9,10,30]:
            result = 'Winner'
        else:
            result = 'Loser'
        message = 'title of surprise '+str(surprise_id)+' Click No.' +'1'+' Result :'+result
        return HttpResponse(message)