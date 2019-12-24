from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام', default=None)
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    grade = models.FloatField(max_length=20, verbose_name='کلاس', default=None)
    image = models.ImageField(verbose_name='عکس', default=None)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.grade)


class TopTeacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام', default=None)
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    grade = models.FloatField(max_length=20, verbose_name='کلاس', default=None)
    image = models.ImageField(verbose_name='عکس', default=None)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.grade)
    

class TopStudent(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام', default=None)
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    grade = models.FloatField(max_length=20, verbose_name='کلاس', default=None)
    image = models.ImageField(verbose_name='عکس', default=None)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='معلم')

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.grade)


class New(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان', default=None)
    text = models.TextField(verbose_name='متن', default=None)
    date_time = models.DateTimeField(verbose_name='تاریخ و زمان')

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(verbose_name='عکس')
