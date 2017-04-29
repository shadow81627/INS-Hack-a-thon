from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Course

def index(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'degrees/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'degrees/detail.html', {'course': course})

