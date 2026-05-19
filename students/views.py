from django.shortcuts import render, get_object_or_404, redirect
from formations.models import Formation
from .models import StudentProfile


# Create your views here.

def enrollToFormation(request, id):
    student = get_object_or_404(StudentProfile, user__id=id)
    if request.method == "POST":
        formation_id = request.POST.get("formation_id")
        formation = get_object_or_404(Formation, id=formation_id)
        student.formation = formation
        student.save()
        return redirect("enrollmentsList")
    return render(request, 'formationsList.html')
