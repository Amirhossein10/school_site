from django.shortcuts import render

from base.models import TopStudent, TopTeacher, New, Picture

def index(request):
    top_students = TopStudent.objects.all()[0:3]
    top_teachers = TopTeacher.objects.all()[0:3]
    pictures = Picture.objects.all()[0:8]
    news = New.objects.all()[0:3]
    context = {'top_students': top_students,
               'top_teachers': top_teachers,
               'pictures': pictures,
               'news': news}

    return render(request, 'index.html', context)

def gallery(request):
    pictures = Picture.objects.all()[:]
    context = {'pictures': pictures}
    return render(request, 'gallery.html', context)

def news(request):
    news = New.objects.all()[:]
    context = {'news': news}
    return render(request, 'news.html', context)

def top_students_page(request):
    top_students = TopStudent.objects.all()[:]
    context = {'top_students': top_students}
    return render(request, 'top_students.html', context)

def contact_us(request):
    return render(request, 'contact_us.html')

def about_school(request):
    return render(request, 'about_school.html')
