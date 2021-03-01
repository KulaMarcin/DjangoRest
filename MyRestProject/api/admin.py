from django.contrib import admin
from . models import Car, Person, Employee, Game, Student

# Register your models here.
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Game)
admin.site.register(Student)
