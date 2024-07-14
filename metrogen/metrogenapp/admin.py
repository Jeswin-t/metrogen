from django.contrib import admin
from .models import login
admin.site.register(login)
from .models import cust_reg
admin.site.register(cust_reg)
from .models import emp_reg
admin.site.register(emp_reg)
from .models import Stationlist
admin.site.register(Stationlist)
from .models import Vehicles
admin.site.register(Vehicles)
from .models import Transportation
admin.site.register(Transportation)
from .models import Homestay
admin.site.register(Homestay)
from .models import Fair
admin.site.register(Fair)
from .models import AddJobs
admin.site.register(AddJobs)
from .models import Jobapply
admin.site.register(Jobapply)
from .models import BookTicket
admin.site.register(BookTicket)
from .models import BookTransportations
admin.site.register(BookTransportations)
from .models import Feedback
admin.site.register(Feedback)
from .models import AllStation
admin.site.register(AllStation)
from .models import Timming
admin.site.register(Timming)
# Register your models here.
