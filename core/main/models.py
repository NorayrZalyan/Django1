from django.db import models

# Create your models here.
class Header(models.Model):
    CompanyName = models.CharField('CompanyName' , max_length=50 , default='CompanyName')
    page_name = models.CharField(' page name' , max_length=50)
    name = models.CharField('name' , max_length=50)
    def __str__(self):
        return self.name




class showcase(models.Model):
    name = models.CharField('img name' , max_length=20,default='aaaa')
    img = models.ImageField('img' , upload_to='media')
    def __str__(self):
        return self.name
class showcase2(models.Model):
    name2 = models.CharField('img name' , max_length=20)
    img2 = models.ImageField('img' , upload_to='media')
    def __str__(self):
        return self.name2





class services(models.Model):
    p = models.CharField('p' , max_length=100)
    text = models.TextField('text')
    def __str__(self):
        return self.p
    



class designers(models.Model):
    p = models.CharField('p' , max_length=150)
    text = models.TextField('text')
    def __str__(self):
        return self.p
class designers_img(models.Model):
    name = models.CharField('name' , max_length=50)
    img = models.ImageField('img' , upload_to='media')
    job_title = models.CharField('job title' , max_length=100 , default=' ')
    about = models.TextField(' about ')
    def __str__(self):
        return self.name
    







class packages(models.Model):
    name = models.CharField('name' , max_length=10)
    price = models.IntegerField('price' , default=199)
    def __str__(self):
        return self.name
class pro(models.Model):
    pname = models.CharField('name' , max_length=10 , default=' ')
    pprice = models.IntegerField('price' , default=199)
    def __str__(self):
        return self.pname


class advantage(models.Model):
    advantage = models.CharField('advantage' , max_length=100)
    def __str__(self):
        return self.advantage
class proAdvantage(models.Model):
    padvantage = models.CharField('advantage' , max_length=70)
    def __str__(self):
        return self.padvantage

