from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def courses(request):
    if request.method == "POST":
        print(request.POST)
        errors = Course.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        Course.objects.create(
            name = request.POST["name"],
            description = request.POST["description"]
        )        
        return redirect('/')
    else:
        context = {
            "all_courses": Course.objects.all()
        }
        return render(request, "courses.html", context)

def delete_course(request, course_id):
    if request.method == "POST":
        course_to_delete = Course.objects.get(id=course_id)
        course_to_delete.delete()

        return redirect('/')
        
    context = {
        "delete_course": Course.objects.get(id=course_id)
    }

    return render(request, "delete-course.html", context)