from django.shortcuts import render, get_object_or_404, redirect
from .models import Formation

# Create your views here.


def makeFormation(request):
    if request.method == "POST":
        formation_name = request.POST.get("formation_name")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        formation = Formation(
            formation_name=formation_name,
            description=description,
            duration=duration
        )
        formation.save()
        return redirect("formationsList")
    return render(request, 'makeFormation.html')


def mdifyFormation(request,id):
    formation = get_object_or_404(Formation, id=id)
    if request.method == "POST":
        formation_name = request.POST.get("formation_name")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        if formation_name: formation.formation_name = formation_name
        if description: formation.description = description
        if duration: formation.duration = duration
        formation.save()
        return redirect("formationsList")
    return render(request, 'makeFormation.html', {"formation": formation})


def removeFormation(request,id):
    formation = get_object_or_404(Formation, id=id)
    if request.method == "POST":
        formation.delete()
        return redirect("formationsList")
    return render(request, 'makeFormation.html', {"formation": formation})