from django.shortcuts import render



def base(request):
    user = request.user
    data = {'user':user}
    return render(request,'base.html',data)