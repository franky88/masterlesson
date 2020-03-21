from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Block(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    block_name = models.CharField(max_length=120, verbose_name='section name')
    def __str__(self):
        return self.block_name
class Disability(models.Model):
    type_of_dis = models.CharField(max_length=250, verbose_name='type of disability', unique=True)
    class Meta:
        verbose_name_plural = 'disabilities'
    def __str__(self):
        return self.type_of_dis
class StudentName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    f_name = models.CharField(max_length=60, verbose_name='first name')
    m_name = models.CharField(max_length=60, verbose_name='middle_name', blank=True)
    l_name = models.CharField(max_length=60, verbose_name='last name')
    e_name = models.CharField(max_length=60, verbose_name='extension name', blank=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name='birth day', help_text='YYYY-mm-dd')
    # disability = models.ForeignKey(Disability, on_delete=models.CASCADE, verbose_name='child diagnosis', blank=True, null=True)
    disability = models.ManyToManyField(Disability)
    school_status = models.BooleanField(default=True, verbose_name='schooling status')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True, null=True, verbose_name='section')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='added')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')
    class Meta:
        ordering = ['-timestamp']
    def calculate_age(self):
        today = date.today()
        born = self.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age
    def full_name(self):
        if self.m_name == False:
            fullname = "%s, %s %s"%(self.l_name, self.f_name, self.e_name)
        elif self.e_name == False:
            fullname = "%s, %s %s"%(self.l_name, self.f_name, self.m_name)
        elif self.m_name == False and self.e_name == False:
            fullname = "%s, %s"%(self.l_name, self.f_name)
        else:
            fullname = "%s, %s %s %s"%(self.l_name, self.f_name, self.m_name, self.e_name)
        return fullname
    def __str__(self):
        return self.full_name().title()