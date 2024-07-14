from django.db import models
class login(models.Model):
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    utype=models.CharField(max_length=20)

class cust_reg(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    pincode = models.IntegerField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    district = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)

class emp_reg(models.Model):
    ename = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    salary = models.IntegerField()
    email = models.CharField(max_length=20)
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)

# class Stations(models.Model):
#     station_id=models.IntegerField(primary_key=True)
#     stations=models.CharField(max_length=20)
class Stationlist(models.Model):
    station_id = models.IntegerField(primary_key=True)
    stations=models.CharField(max_length=20)

class Vehicles(models.Model):
    Vehicle_id = models.IntegerField(primary_key=True)
    Vehiclename = models.CharField(max_length=20)
    Type = models.CharField(max_length=20,default="")
class Transportation(models.Model):
    trspt_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    adrs = models.CharField(max_length=20)
    station = models.CharField(max_length=20)
    adhar = models.IntegerField()
    driving = models.CharField(max_length=20)
    vehicle =  models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    capacity =  models.CharField(max_length=20)
    regnum =  models.CharField(max_length=20)
    fon =  models.IntegerField()
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    SeatingCapacity=models.CharField(max_length=20,default="")
    type='Transportation'
    AdhaarNumber=models.FileField(upload_to='metrogenapp/media/Transportor',default='')
    CarPhoto = models.FileField(upload_to='metrogenapp/media/Transportor', default='')
    PersonalPhoto=models.FileField(upload_to='metrogenapp/media/Transportor', default='')
    IsActive =models.CharField(max_length=20,default='False')

class Homestay(models.Model):
    stay_id = models.IntegerField(primary_key=True)
    cname= models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    Phone = models.IntegerField()
    desc = models.CharField(max_length=50)
    File = models.FileField()

class Fair(models.Model):
    From = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    Fair = models.IntegerField()
class AddJobs(models.Model):
    jobid=models.IntegerField(primary_key=True)
    ref= models.CharField(max_length=20)
    vaccancy=models.IntegerField(default=0)
    position=models.CharField(max_length=20)
    quali=models.CharField(max_length=20)
    start=models.DateField()
    end=models.DateField()
class Jobapply(models.Model):
    job_Applied_id=models.IntegerField(primary_key=True)
    job_id= models.IntegerField()
    cus_id=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default="")
    file=models.FileField(default='')
    Cust_name=models.CharField(max_length=20,default='')
    Cust_phone=models.IntegerField(default=0)
    Cust_email=models.CharField(max_length=20,default='')
    ref=models.CharField(max_length=20,default='')
    post=models.CharField(max_length=20,default='')

class BookTicket(models.Model):
    Ticket_id=models.IntegerField(primary_key=True)
    cid=models.CharField(max_length=20)
    fromsta=models.CharField(max_length=20)
    tosta = models.CharField(max_length=20)
    tickett=models.IntegerField()
    total=models.IntegerField()
    bdate=models.DateField()
class BookTransportations(models.Model):
    bkid=models.IntegerField(primary_key=True)
    cid=models.IntegerField()
    taid=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)

class Feedback(models.Model):
    Feedback_id=models.IntegerField(primary_key=True)
    cust_id=models.IntegerField()
    fdate=models.DateField()
    feedback=models.CharField(max_length=50)
class AllStation(models.Model):
    vehicle_id=models.IntegerField(primary_key=True)
    vehicle=models.CharField(max_length=20)

class Timming(models.Model):
    Updated_Date=models.DateField()
    file=models.FileField(upload_to='metrogenapp/file')

# class BookTransportation(models.Model):


# Create your models here.
