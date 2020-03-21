from django.contrib import admin
from .models import StudentName, Block, Disability
# Register your models here.
@admin.register(StudentName)
class StudentListAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'birth_date', 'calculate_age', 'block', 'timestamp', 'updated')
    list_filter = ('block', 'school_status')
# admin.site.register(StudentName, StudentList)
@admin.register(Block)
class BlockListAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Disability)
class DisabilityAdmin(admin.ModelAdmin):
    list_display = ('__str__',)