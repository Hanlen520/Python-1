from django.db import models


# models.py文件是与数据库相关的文件
# Create your models here.
# 新建Person类，继承自models.Model
# 一个类对应数据库中的一张表
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    # qq = models.CharField(max_length=10)
    # addr = models.TextField(null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        # 这里的self，就是指当前类
        return self.headline


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    # score = models.IntegerField()
    pub_date = models.DateField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', editable=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



