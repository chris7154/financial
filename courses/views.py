from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render (request, 'courses/course_list.html', {'courses':courses})
    return redirect('course_details')

def course_details(request, pK):
    course = get_object_or_404(Course, pk=pK)
    return render(request, 'courses/course_details.html', {'course':course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Moved redirect to the correct indentation level
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})


def course_update(request, pK):
    course = get_object_or_404(Course, pK=pK)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = course)
        if form.is_valid():
            form.save()
        return redirect('course_detail', pk=course.pk)  # Redirect to course detail page after successful update
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/course_update.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')  # Redirect to course list page after successful deletion
    
    return render(request, 'courses/course_delete.html', {'course': course})