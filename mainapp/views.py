from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .email import *
# Create your views here.

@csrf_exempt
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
        sendmail(name,email,event)
        return redirect("success")
    return render(request,"reg-solo.html")

@csrf_exempt
def registerTeam(request):
    if request.method=="POST":
        name=request.POST.get("Name","")
        number=request.POST.get("Phone","")
        email=request.POST.get("Email","")
        college=request.POST.get("ticket-a","")
        event=request.POST.get("my-dropdown","")
        year_of_study=request.POST.get("ticket-c",None)
        team_count=request.POST.get("ticket-b",None)
        head_name=request.POST.get("head","")
        member_1=request.POST.get("mem1","")
        member_2=request.POST.get("mem2","")
        member_3=request.POST.get("mem3","")
        r=Registration(name=name,number=number,email=email,college=college,event_name=event,year_of_study=year_of_study,team_count=team_count,head_name=head_name,member_1=member_1,member_2=member_2,member_3=member_3)
        r.save()
        sendmail(name,email,event)
        return redirect("success")
    return render(request,"reg-team.html")

@csrf_exempt
def registerFifa(request):
    if request.method=="POST":
        print(request.POST)
        email=request.POST.get("Email","")
        team_name=request.POST.get("Team-Name","")
        college_name=request.POST.get("ticket-a","")
        member_name1=request.POST.get("Mem-Name-1","")
        member_name2=request.POST.get("Mem-Name-2","")
        mem1_phno=request.POST.get("Phone-1","")
        mem2_phno=request.POST.get("Phone-2","")
        online_eve_name=request.POST.get("my-dropdown","")
        year_of_study=request.POST.get("ticket-c",0)
        attachment=request.FILES.get("filename","")
        r=FifaRegistration(email=email,team_name=team_name,college_name=college_name,member1=member_name1,member2=member_name2,phone1=mem1_phno,phone2=mem2_phno,event=online_eve_name,year_of_study=year_of_study)
        r.save()
        sendmail(member_name1,email,online_eve_name)
        return redirect("success")
        
    return render(request,"reg-fifa.html")

@csrf_exempt
def registerCod(request):
    if request.method=="POST":
        
        team_name=request.POST.get("TName",""),
        lead_name=request.POST.get("Name","")
        lead_ph_no=request.POST.get("Phone","")
        mem2=request.POST.get("Name2","")
        mem3=request.POST.get("Name3","")
        email=request.POST.get("Email","")
        event_name=request.POST.get("my-dropdown","")
        year=request.POST.get("ticket-c")
        payment=request.FILES.get("filename","")
        college_name=request.POST.get("ticket-a","")
        r=CodRegistration(
            team_name=team_name,
            lead_name=lead_name,
            lead_ph_no=lead_ph_no,
            mem2=mem2,
            mem3=mem3,
            email=email,
            event_name=event_name,
            year=year,
            college_name=college_name
        )
        r.save()
        sendmail(lead_name,email,event_name)
        return redirect("success")
    
        
    return render(request,"reg_cod.html")

@csrf_exempt
def registerValo(request):
    if request.method=="POST":
        teamname=request.POST.get("tName","")
        leadname=request.POST.get("lName","")
        leadnumber=request.POST.get("lPhone","")
        riotid=request.POST.get("rName","")
        discordid=request.POST.get("dName","")
        mem2ph=request.POST.get("Name2ph","")
        mem2=request.POST.get("Name2","")
        mem2dis=request.POST.get("Name2dis","")
        mem3=request.POST.get("Name3","")
        mem3dis=request.POST.get("Name3dis","")
        mem4=request.POST.get("Name4","")
        mem4dis=request.POST.get("Name4dis","")
        mem5=request.POST.get("Name5","")
        mem5dis=request.POST.get("Name5dis","")
        email=request.POST.get("Email","")
        college_name=request.POST.get("ticket-a","")
        event_name=request.POST.get("my-dropdown","")
        year=request.POST.get("ticket-c","")
        

        r=ValoRegistration(
            teamname=teamname,
            leadname=leadname,
            leadnumber=leadnumber,
            riotid=riotid,
            discordid=discordid,
            mem2=mem2,
            mem2dis=mem2dis,
            mem2ph=mem2ph,
            mem3=mem3,
            mem3dis=mem3dis,
            mem4=mem4,
            mem4dis=mem4dis,
            mem5=mem5,
            mem5dis=mem5dis,
            event_name=event_name,
            email=email,
            year=year,
            college_name=college_name,
           
        )
        r.save()
        sendmail(leadname,email,event_name)
        return redirect("success")
    return render(request,"reg_valo.html")

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def eventTagline(request):
    return render(request,"event-tagline.html")

def photomania(request):
    return render(request,"photomania.html")

def geekspeak(request):
    return render(request,"geekspeak.html")

def algolia(request):
    return render(request,"algolia.html")

def codehunt(request):
    return render(request,"codehunt.html")

def sharktank(request):
    return render(request,"sharktank.html")

def s2s(request):
    return render(request,"s2s.html")

def connexions(request):
    return render(request,"connexions.html")

def techtonic(request):
    return render(request,"techtonic.html")

def gamingevent(request):
    return render(request,"gaming-events.html")

def fifa(request):
    return render(request,"fifa.html")

def valorant(request):
    return render(request,"valorant.html")

def cod(request):
    return render(request,"cod.html")

@csrf_exempt
def contact(request):
    if request.method=="POST":
        name=request.POST.get("Name","")
        email=request.POST.get("Email","")
        phone=request.POST.get("phone","")
        message=request.POST.get("message","")
        c=Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        c.save()
        
    return render(request,"contact.html")

def video(request):
    return render(request,"video.html")

def success(request):
    return render(request,"landing-page.html")