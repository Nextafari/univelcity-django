from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Landing page view
@login_required
def dashboard(request):
    return render(
        request,
        'dashboard.html'
    )