from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def registerSolo(request):
    if request.method=="POST":
        name=request.POST.get("Name")
        number=request.POST.get("Phone")
        email=request.POST.get("Email")
        college=request.POST.get("ticket-a")
        event=request.POST.get("my-dropdown")
        year_of_study=request.POST.get("ticket-c")
        r=Registration(name=name,number=number,email=email,college=college,event_name=event,year_of_study=year_of_study)
        r.save()
        return HttpResponse("<h1>Success</h1>")
    return render(request,"reg-solo.html")

def registerTeam(request):
    if request.method=="POST":
        name=request.POST.get("Name")
        number=request.POST.get("Phone")
        email=request.POST.get("Email")
        college=request.POST.get("ticket-a")
        event=request.POST.get("my-dropdown")
        year_of_study=request.POST.get("ticket-c")
        team_count=request.POST.get("ticket-b")
        head_name=request.POST.get("head")
        member_1=request.POST.get("mem1")
        member_2=request.POST.get("mem2")
        member_3=request.POST.get("mem3")
        r=Registration(name=name,number=number,email=email,college=college,event_name=event,year_of_study=year_of_study,team_count=team_count,head_name=head_name,member_1=member_1,member_2=member_2,member_3=member_3)
        r.save()
        return HttpResponse("<h1>Success</h1>")
    return render(request,"reg-team.html")