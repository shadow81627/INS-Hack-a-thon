from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Course

def index(request):
    course_list = Course.objects.all()
    suggest1_list = Course.objects.order_by('?')[:4]
    suggest2_list = Course.objects.order_by('?')[:4]
    suggest3_list = Course.objects.order_by('?')[:4]
    context = {'course_list': course_list, 'suggest1_list': suggest1_list, 'suggest2_list': suggest2_list, 'suggest3_list': suggest3_list,}
    return render(request, 'degrees/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'degrees/detail.html', {'course': course})

