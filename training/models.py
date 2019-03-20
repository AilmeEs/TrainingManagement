from django.db import models
from django.conf import settings


# Create your models here.
#公司表
class Company(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name


# 部门

class Department(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='departments')
    def __str__(self):
        return self.name
#职位表
class Position(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    def __str__(self):
        return self.name



# 位置

class Position(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()



# 个人信息

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女")
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=11)
    email = models.EmailField()
    entry = models.DateField()
    leave = models.DateField(blank=True, null=True)
    cardnumber = models.CharField(max_length=20, blank=True)
    idnumber = models.CharField(max_length=12, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='depart_emp')
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name='position_emp')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    def __str__(self):
        return self.name


# 课程
class Course(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    most = models.PositiveSmallIntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

    teacher = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                   related_name='course')
    students = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 related_name='courses')

#考勤内容

class Duty(models.Model):
    name = models.CharField(max_length=50)


# 日志
class Note(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='notes')
    dutys = models.ManyToManyField(Duty, related_name='notes')



# 文章
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    auth = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name='posts')
    def __str__(self):
        return self.title


# 登陆
class Logging(models.Model):
    login = models.DateTimeField()
    logout = models.DateTimeField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name='loggings')
