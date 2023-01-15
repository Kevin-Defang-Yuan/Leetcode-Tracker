from django.contrib import admin
from .models import Question, Collection, Task
# Register your models here.

admin.site.register(Question)
admin.site.register(Collection)
admin.site.register(Task)
