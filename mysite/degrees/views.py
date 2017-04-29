from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Course

def index(request):
    course_list = Course.objects.all()
    suggest_list = Course.objects.order_by('code')[:12]
    context = {'course_list': course_list, 'suggest_list': suggest_list}
    return render(request, 'degrees/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'degrees/detail.html', {'course': course})

