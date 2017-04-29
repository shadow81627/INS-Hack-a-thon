from django.contrib import admin

from .models import Course
from .models import Offering
from .models import Degree
from .models import Campus
from .models import Requirement

admin.site.register(Course)
admin.site.register(Offering)
admin.site.register(Degree)
admin.site.register(Campus)
admin.site.register(Requirement)
