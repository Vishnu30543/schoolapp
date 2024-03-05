from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login/')       # for function based we can give directly
def homepage(request):
    return render(request, 'index.html')


def logoutUser(request):
    print("came here")
    return render(request, 'logout.html')
