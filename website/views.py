from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment


def home(request):
    return render(request, 'home.html')


def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        Enrollment.objects.create(
            course=course,
            student_name=request.POST.get('student_name'),
            student_email=request.POST.get('student_email'),
            student_phone=request.POST.get('student_phone'),
            message=request.POST.get('message')
        )
        return redirect('course_list')

    return render(request, 'enroll.html', {'course': course})