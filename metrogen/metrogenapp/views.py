from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate,login
# from .models import login
from .models import login as loginval
from .models import Stationlist
from .models import cust_reg
from django.http import HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage
from .models import Vehicles
from datetime import date
from datetime import datetime
import datetime
from django.contrib import messages
from .models import *
from .models import Homestay
from .models import Fair
from .models import AddJobs
from .models import BookTransportations
from .models import Jobapply
from .models import Feedback
from .models import AllStation
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

def community(request):
    return HttpResponse("This is index page")
def CommonHome(request):
    msg=''
    if 'usernameval' in request.session:
        user = request.session['usernameval']
        user_obj = loginval.objects.get(uname=user)
        transportation = Transportation.objects.filter(email=user)
        user_details = cust_reg.objects.filter(email=user)
        if user_obj.utype == "Customer":
            return render(request, 'CustomerHome.html', {'msg': msg})
        if user_obj.utype == "Admin":
            return render(request, 'AdminHome.html')
        if user_obj.utype == "Transportation":
            return render(request, 'TransportationHome.html')
        if user_obj.utype == "Employee":
            return render(request, 'EmployeeHome.html')
    # if 'trnspt_id' in request.session:
    #     user = request.session['cust_id']
    #     user_obj = loginval.objects.filter(uname=user)
    #     if user_obj.utype == "Customer":
    #         return render(request, 'CustomerHome.html', {'msg': msg})
    #     if user_obj.utype == "Admin":
    #         return render(request, 'AdminHome.html')
    #     if user_obj.utype == "Transportation":
    #         return render(request, 'TransportationHome.html')
    #     if user_obj.utype == "Employee":
    #         return render(request, 'EmployeeHome.html')


    return render(request, 'CommonHome.html')


def Gallery(request):
    return render(request, 'gallery.html')


def Home(request):
    return render(request, 'CommonHome.html')


def AdminHome(request):
    return render(request, 'AdminHome.html')


def TransportationHome(request):
    return render(request, 'TransportationHome.html')


def Customer_Home(request):
    return render(request, 'CustomerHome.html')


def EmployeeHome(request):
    return render(request, 'EmployeeHome.html')


def About_Us(request):
    return render(request, 'about.html')


def lgdata(request):
    current = date.today()
    job = AddJobs.objects.filter(end=current).delete()
    msg=''
    name=''
    passwordd = ''
    request.session['cust_id']=''
    if request.method == "POST":
        usernameval = request.POST.get('userval')
        passwordd = request.POST.get('passval')
        try:
            if not usernameval or not passwordd:
                msg='Both Username and Password are required.'
                return render(request, 'loginchk.html', {'msg': msg})
            user_obj=loginval.objects.get(uname=usernameval)
            transportation=Transportation.objects.filter(email=usernameval)
            user_details = cust_reg.objects.filter(email=usernameval)
            if user_details.exists():
                request.session['usernameval'] = usernameval
                data_list = ""  # Create the data_list outside the loop

                for i in user_details:
                    data_list=i.cid

                request.session['cust_id'] = data_list
            if request.session['cust_id'] is  None:
                return HttpResponse(data_list)
            # if request.session['cust_id'] is  None:
            #     return HttpResponse('fail')
            if user_obj is None:
                msg="User not found"
                return render(request,'loginn.html',{'msg':msg})
            if transportation.exists():
                trspt_id=""
                for i in transportation:
                    trspt_id=i.trspt_id

                request.session['trnspt_id'] = trspt_id
                for val in transportation:
                    istrue = val.IsActive
                if istrue == 'False' :
                    messages.success(request,'Administrator Processing Your Signup Request,Kindly wait!')

                    return redirect('/chk')
            if user_obj.password == passwordd:

                if user_obj.utype=="Customer":
                    return render(request,'CustomerHome.html',{'msg':msg})
                if user_obj.utype=="Admin":
                    return render(request,'AdminHome.html')
                if user_obj.utype=="Transportation":
                    return render(request,'TransportationHome.html')
                if user_obj.utype=="Employee":
                    return render(request,'EmployeeHome.html')

            else:
                msg="password Entered Is Wrong"
                return render(request, 'loginchk.html',{'msg':msg})

        except Exception:
                msg='invalid Username'
                return render(request, 'loginchk.html',{'msg':msg})
    else:
        return render(request, 'loginchk.html')

def Customer_Registration(request):
    request.session['my_variable'] = 'Hello, World!'
    msg = ""
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        district = request.POST.get("district")
        location = request.POST.get("location")
        email = request.POST.get("Email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("Password")
        type = "Customer"
        if cust_reg.objects.filter(email=email):
            msg = "Email already registered."
            return render(request, 'CustomerRegistration.html', {"msg": msg})

        else:
            insert = cust_reg.objects.create(cname=cname, address=address, pincode=pincode, gender=gender, age=age,
                                             district=district, location=location, email=email, mobile=mobile,
                                             password=password)
            loginsert=loginval.objects.create(uname=email,password=password,utype='Customer')
            messages.success(request,"Registered successfully")
            return HttpResponseRedirect('/')
            # return render(request, 'CommonHome.html', {"msg": msg})
    else:
        return render(request, 'CustomerRegistration.html', {"msg": msg})

from .models import Transportation
def TransportationSignUp(request):
    station=Stationlist.objects.all()
    vehicle=AllStation.objects.all()
    if request.POST:
        name = request.POST.get("name")
        adrs = request.POST.get("adrs")
        station = request.POST.get("dist")
        adhar = request.POST.get("adhar")
        driving = request.POST.get("driving")
        vehicle = request.POST.get("vehicle")
        model = request.POST.get("model")
        capacity = request.POST.get("capacity")
        regnum = request.POST.get("regnum")
        fon = request.POST.get("fon")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        CarPhoto = request.FILES.get('CarPhoto')
        type = "Transportation"
        if Transportation.objects.filter(regnum=regnum):
            msg = "Vehicle already registered."
            return render(request, 'TransportationSignUp.html', {"msg": msg})
        else:
            Transportation.objects.create(name=name,adrs=adrs,station=station,adhar=adhar,driving=driving,vehicle=vehicle,model=model,capacity=capacity,regnum=regnum,fon=fon,email=email,password=password,CarPhoto=CarPhoto)
            loginval.objects.create(uname=email,password=password,utype=type)
            messages.success(request,"Registered successfully")
            return HttpResponseRedirect('/')

    else:
        return render(request, 'TransportationSignUp.html',{"station":station,"vehicle":vehicle})


def AdminAddEmployee(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("hname")
        address = request.POST.get("address")
        desig = request.POST.get("desig")
        salary = request.POST.get("salary")
        email = request.POST.get("email")
        mobile = request.POST.get("phone")
        password = request.POST.get("pass")
        type = "Employee"
        if emp_reg.objects.filter(email=email):
            msg = "This Email already registered."
            return render(request, 'AdminAddEmployee.html.html', {"msg": msg})
        else:
                data=emp_reg.objects.create(ename=cname,address=address,designation=desig,salary=salary,email=email,mobile=mobile,password=password)
                datas=loginval.objects.create(uname=email,password=password,utype=type)
                msg="Employee Registered Successfully"
                return render(request,'AdminHome.html',{'msg':msg})
    else:
        return render(request,'AdminAddEmployee.html')




def AdminViewCustomers(request):
    data = ""
    cust=cust_reg.objects.all()
    return render(request, "AdminViewCustomers.html", {"data": cust})


def EmployeeAddStations(request):
    msg =""

    if request.POST:
        na = request.POST.get("cat_name")
        if Stationlist.objects.filter(stations=na):
            msg="Station Already Added"
            return render(request, 'EmployeeAddStations.html', {'msg': msg})
        else:
            insert=Stationlist.objects.create(stations=na)
            msgg ="Station Added Successfully."
            return render(request,'EmployeeHome.html',{'msg':msgg})
    else:

        return render(request, 'EmployeeAddStations.html')
def AdminAddStations(request):
    msg =""

    if request.POST:
        na = request.POST.get("cat_name")
        if Stationlist.objects.filter(stations=na):
            msg="Station Already Added"
            return render(request, 'AdminAddStations.html', {'msg': msg})
        else:
            insert=Stationlist.objects.create(stations=na)
            msgg ="Station Added Successfully."
            return render(request,'AdminHome.html',{'msg':msgg})
    else:

        return render(request, 'AdminAddStations.html')


def AdminAddStay(request):
    msg = ""
    # c.execute("select * from station")
    # data = c.fetchall()
    stations=Stationlist.objects.all()
    if request.POST:
        cname = request.POST.get("hname")
        address = request.POST.get("address")
        dist = request.POST.get("dist")
        location = request.POST.get("location")
        Phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        if request.FILES.get("file"):
            myfile = request.FILES.get("file")
            if Homestay.objects.filter(cname=cname):
                msg="Already Added.."
                return render(request,'AdinAddStay.html',{"msg":msg})
            else:
                insert=Homestay.objects.create(cname=cname,address=address,dist=dist,location=location,Phone=Phone,desc=desc,File=myfile)
                msg = "Stay Details Added Successfully"
                return render(request,"AdminHome.html",{"msg":msg})
    else:
        return render(request, 'AdminAddStay.html',{'cat':stations})


def EmployeeAddFair(request):
    msg = ""
    station=Stationlist.objects.all()
    if request.POST:
        froms = request.POST.get("From")
        to = request.POST.get("To")
        fair = request.POST.get("Fair")
        try:
            if froms == to:
                msg = "From And To Stations Cannot Be Same."
                return render(request,'EmployeeAddFair.html',{'msg':msg,"cat": station})
            if Fair.objects.filter(From=froms,To=to):
                msg="Fair Already Added..."
                return render(request, 'EmployeeAddFair.html', {'msg': msg,"cat": station})
            else:
                 main=Fair.objects.create(From=froms,To=to,Fair=fair)
                 msg = "Fair Added Successfully."
                 return render(request, 'EmployeeAddFair.html', {'msg': msg,"cat":station})
        except Exception as e:
            print(e)
            return render(request, 'EmployeeAddFair.html', {'msg': e})

    else:

        return render(request, 'EmployeeAddFair.html', { "cat": station})

def AdminAddFair(request):
    msg = ""
    station=Stationlist.objects.all()
    if request.POST:
        froms = request.POST.get("From")
        to = request.POST.get("To")
        fair = request.POST.get("Fair")
        try:
            if froms == to:
                msg = "From And To Stations Cannot Be Same."
                return render(request,'AdminAddFair.html',{'msg':msg,"cat": station})
            if Fair.objects.filter(From=froms,To=to):
                msg="Fair Already Added..."
                return render(request, 'AdminAddFair.html', {'msg': msg,"cat": station})
            else:
                 main=Fair.objects.create(From=froms,To=to,Fair=fair)
                 msg = "Fair Added Successfully."
                 return render(request, 'AdminAddFair.html', {'msg': msg,"cat":station})
        except Exception as e:
            print(e)
            return render(request, 'AdminAddFair.html', {'msg': e})

    else:

        return render(request, 'AdminAddFair.html', { "cat": station})


def AdminViewFeedback(request):
    # data = request.session['cust_id']
    cust_id=0
    select = Feedback.objects.all()
    if select is None :
        return HttpResponse('fail')
    for i in select:
        cust_id=i.cust_id
    name=cust_reg.objects.filter(cid=cust_id)
    select = Feedback.objects.all()
    return render(request, "AdminViewFeedback.html", {"data": select,'name':name})


def AdminViewJob(request):
    data = ""
    select=AddJobs.objects.all()
    return render(request, "AdminViewJob.html", {"data": select})


def AdminViewTransportation(request):
    data = ""
    select=Transportation.objects.all()
    return render(request, "AdminViewTransportation.html", {"data": select})

def EmployeeViewTicket(request):
    select=BookTicket.objects.all()
    name=""
    id=""
    for i in select:
        id=i.cid
    info=cust_reg.objects.filter(cid=id)
    return render(request,'EmployeeViewTicket.html',{'data':select,'name':info})


def EmployeeAddJob(request):
    # sid = request.session['eid']
    msg = ""
    if request.POST:
        ref = request.POST.get("ref")
        vaccancy = request.POST.get("vaccancy")
        position = request.POST.get("position")
        quali = request.POST.get("quali")
        start = request.POST.get("start")
        end = request.POST.get("end")
        if AddJobs.objects.filter(ref=ref):
            msg = "Job Details already added."
            return render(request,'EmployeeAddJob.html',{'msg':msg})
        else:
            insert=AddJobs.objects.create(ref=ref,vaccancy=vaccancy,position=position,quali=quali,start=start,end=end)
            msg = "Job Details Added Successfully"
            return render(request, 'EmployeeHome.html', {'msg': msg})
    else:
        return render(request, 'EmployeeAddJob.html', {"msg": msg})


def AdminViewJobApplications(request):
    select=''
    details=''
    data=0
    cust_id=request.session['cust_id']

    data=Jobapply.objects.filter(status='Applied')



    if request.GET:
        action=request.GET.get('action')
        id=request.GET.get('id')
        job_id =request.GET.get('job_id')
        cust_number = request.GET.get('cus_id')
        details = cust_reg.objects.get(cid=cust_number)
        if action == 'Accept':
            data = emp_reg.objects.create(ename=details.cname, address=details.address, designation="Employee", salary=0, email=details.email,
                                          mobile=details.mobile, password=details.password)

            datas = loginval.objects.get(uname=details.email)
            job=Jobapply.objects.filter(job_Applied_id=cust_number)
            job.delete()
            datas.utype='Employee'
            datas.save()
            delete=cust_reg.objects.get(cid=cust_number)
            delete.delete()
            job =AddJobs.objects.get(jobid=job_id)
            job.vaccancy -= 1
            job.save()
            if job.vaccancy <=0:
                job.delete()
            return redirect('/AdminViewJobApplications')
            subject = 'Offer letter'
            message = 'Greetings from Kochi Metro.. Your application for is accepted.You can login with your credentials'
            recipient = details.email
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')


            return render(request,'AdminHome.html')
        if action =='Reject':
            job=Jobapply.objects.filter(job_Applied_id=id)
            job.delete()
            return redirect('/AdminViewJobApplications')
            subject = 'Kochi Metro'
            message = 'from Kochi Metro.. Your request has been denied.apply again later'
            recipient = details.email
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')






    # sid = request.session['eid']
    # data = ""
    # c.execute(
    #     "select * from jobapply inner join career on jobapply.jid = career.jid inner join cust_reg on jobapply.cid = cust_reg.cid where jobapply.status = 'Applied'")
    # data = c.fetchall()
    # if request.GET:
    #     job = data[0][9]
    #     mail = data[0][22]
    #     japplid = request.GET.get('id')
    #     st = request.GET.get('st')
    #     if st == "Accept":
    #         c.execute("update jobapply set status= 'Accept' where jaid = '" + str(japplid) + "'")
    #         db.commit()
    #         msg = "Greetings from Kochi Metro.. Your application for " + job + " will be accepted. Please prepare for the aptitude test"
    #         sendemail(mail, msg)
    #         return HttpResponseRedirect('/EmployeeViewJobApplications/')
    #     else:
    #         c.execute("delete from jobapply  where jaid = '" + str(japplid) + "'")
    #         db.commit()
    #         return HttpResponseRedirect('/EmployeeViewJobApplications/')
    return render(request, "AdminViewJobApplications.html", {"data": data})

def AdminViewTransporterJobApplications(request):
    select=''
    details=''
    data=0
    cust_id=request.session['cust_id']

    data=Transportation.objects.filter(IsActive='False')
    # if data.exists():
    #     for i in data:
    #         cust_id=i.cus_id
    #     details=cust_reg.objects.get(cid=cust_id)
    # else:
    #     messages.success(request,'No New Application')



    if request.GET:
        action=request.GET.get('action')
        id=request.GET.get('id')
        if action == 'Accept':
            Transport=Transportation.objects.get(trspt_id=id)
            Transport.IsActive = 'True'
            Transport.save()
            return redirect('/AdminViewTransporterJobApplications')
            # subject = 'Offer letter'
            # message = 'Greetings from Kochi Metro.. Your application for is accepted.You can login with your credentials'
            # recipient = details.email
            # send_mail(subject,
            #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            # messages.success(request, 'Success!')

            #
            # return render(request,'AdminHome.html')
        if action =='Reject':
            Transport=Transportation.objects.get(trspt_id=id)
            Transport.IsActive = 'Rejected'
            Transport.save()
            return redirect('/AdminViewTransporterJobApplications')
            # subject = 'Kochi Metro'
            # message = 'from Kochi Metro.. Your request has been denied.apply again later'
            # recipient = details.email
            # send_mail(subject,
            #           message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            # messages.success(request, 'Success!')






    # sid = request.session['eid']
    # data = ""
    # c.execute(
    #     "select * from jobapply inner join career on jobapply.jid = career.jid inner join cust_reg on jobapply.cid = cust_reg.cid where jobapply.status = 'Applied'")
    # data = c.fetchall()
    # if request.GET:
    #     job = data[0][9]
    #     mail = data[0][22]
    #     japplid = request.GET.get('id')
    #     st = request.GET.get('st')
    #     if st == "Accept":
    #         c.execute("update jobapply set status= 'Accept' where jaid = '" + str(japplid) + "'")
    #         db.commit()
    #         msg = "Greetings from Kochi Metro.. Your application for " + job + " will be accepted. Please prepare for the aptitude test"
    #         sendemail(mail, msg)
    #         return HttpResponseRedirect('/EmployeeViewJobApplications/')
    #     else:
    #         c.execute("delete from jobapply  where jaid = '" + str(japplid) + "'")
    #         db.commit()
    #         return HttpResponseRedirect('/EmployeeViewJobApplications/')
    return render(request, "AdminViewTransporterJobApplications.html", {"data": data})
def EmployeeViewTransporation(request):
    select=Transportation.objects.all()
    return render(request,'EmployeeViewwTransportation.html',{'data':select})
def EmployeeViewTransporationConfirmed(request):

    select=BookTransportations.objects.filter(status='Accepted')
    for i in select:
        trast_id=i.taid
        cust_id=i.cid
    details=Transportation.objects.filter(trspt_id=trast_id)
    cust_name=cust_reg.objects.filter(cid=cust_id)
    return render(request,'EmployeeViewwConfirmedTransportation.html',{'data':select,'details':details,'cust':cust_name})


from .models import BookTicket
def CustomerViewConfimedTransporation(request):
    transportid=0
    data = request.session['cust_id']
    select=BookTransportations.objects.filter(cid=data)
    for i in select:
        transportid=i.taid
    if transportid == 0:
        return render(request,'CustomerViewConfTransporation.html')
    trsprtdetails=Transportation.objects.filter(trspt_id=transportid)
    return render(request,'CustomerViewConfTransporation.html',{'datas':select,'details':trsprtdetails})
def CustomerBookTickets(request):
    cid = request.session['cust_id']
    station=Stationlist.objects.all()
    fairs=Fair.objects.all()
    total_amount=''
    froms=''
    tos=''
    ticket=''

    if 'ADD' in request.POST:
        froms = request.POST['From']
        request.session["froms"] = froms
        tos = request.POST['To']
        request.session["tos"] = tos
        ticket = request.POST.get("ticket")

        if froms == tos:
             msg = "Fairstage Invalid"
        else:
            amount = ''
            select=Fair.objects.filter(From=froms,To=tos)
            if select is None:
                return HttpResponse(fail)
            for i in select:
                amount=i.Fair
            # amount=select.Fair
            total_amount = int(ticket) * int(amount)
            request.session["tm"] = total_amount

    if 'Book' in request.POST:
            cid = request.session['cust_id']
            fromsta = request.session["froms"]
            tosta = request.session["tos"]
            tickett = request.POST.get("ticket")
            request.session["ticket"] = tickett
            total = request.session["tm"]
            bdate = date.today()
            insert = BookTicket.objects.create(cid=cid,fromsta=fromsta,tosta=tosta,tickett=tickett,total=total,bdate=bdate)
            msg="successfully Booked"
            return HttpResponseRedirect("/payment1")
    return render(request, 'CustomerBookTickets.html',{'cat':station,'total_amount':total_amount,'froms':froms,'tos':tos,"ticket":ticket,'fairs':fairs})


def CustomerSearchStay(request):
    c.execute("select * from station")
    station = c.fetchall()
    data = ""
    if request.POST:
        di = request.POST.get('dist')
        c.execute("select * from stay where station = '" + str(di) + "'")
        data = c.fetchall()
    if request.GET:
        stid = request.GET.get('id')
        request.session["stid"] = stid
        return HttpResponseRedirect("/CustomerBookStay/")
    return render(request, 'CustomerSearchStay.html', {"station": station, "data": data})


def payment1(request):
    if request.POST:
        card = request.POST.get("test")
        request.session["card"] = card
        cardno = request.POST.get("cardno")
        request.session["card_no"] = cardno
        pinno = request.POST.get("pinno")
        request.session["pinno"] = pinno
        return HttpResponseRedirect("/payment2")
    return render(request, "payment1.html")


def payment2(request):
    cno = request.session["card_no"]
    amount = request.session["tm"]
    if request.POST:
        # name=request.POST.get("t1")
        # request.session["m"]=name
        # address=request.POST.get("t2")
        # email=request.POST.get("t3")
        # phno=request.POST.get("t4")
        # n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        # print(n)
        # c.execute(n)
        # con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request, "payment2.html", {"cno": cno, "amount": amount})


def payment3(request):
    return render(request, "payment3.html")


def payment4(request):
    return render(request, "payment4.html")


def payment5(request):
    cid=int(request.session['cust_id'])
    val=cust_reg.objects.filter(cid=cid)
    for i in val:
        name=i.cname
    cno = request.session["card_no"]
    today = date.today()
    amount = request.session["tm"]
    froms = request.session["froms"]
    tos = request.session["tos"]
    num = request.session["ticket"]
    return render(request, "payment5.html",
                  {"cno": cno, "today": today, "name": name, "amount": amount, "froms": froms, "tos": tos, "num": num})


def CustomerAddFeedback(request):
    msg = ""
    cid = request.session['cust_id']
    if request.POST:
        a = request.POST.get("pname")
        b = date.today()
        insert=Feedback.objects.create(cust_id=cid,fdate=b,feedback=a)
        msg = "Feedback Added Successfully."
        return render(request, "CustomerAddFeedback.html", {"msg": msg})
    else:
        return render(request, "CustomerAddFeedback.html", {"msg": msg})



def CustomerView(request):
    data = ""

    cid =request.session['cust_id']
    job=AddJobs.objects.all()
    if request.GET:

        jid = request.GET['id']
        request.session["jid"] = jid
        if Jobapply.objects.filter(cus_id=cid,job_id=jid):
            msg="Already registered"
            return render(request,'CustomerViewJob.html',{'msg':msg,"data":job})
        else:
            return HttpResponseRedirect("CustomerUploadResume")
    return render(request, "CustomerViewJob.html", {"data":job})


def TransportationViewBooking(request):
    data = ""
    tid = request.session['trnspt_id']
    select=BookTransportations.objects.filter(taid=tid,status='Booked')
    if request.GET:
        st = request.GET.get('st')
        bk = request.GET.get('id')
        if st == "Accept":
            update=BookTransportations.objects.filter(bkid=bk).update(status="Accepted")
            return render(request,'TransportationViewConfirmedBooking.html',{'data': select})
        if st == "Reject":
            update=BookTransportations.objects.filter(bkid=bk).update(status="Rejected")
            return render(request,'TransportationViewConfirmedBooking.html',{'data': select})
    return render(request, "TransportationViewBooking.html", {"data": select})


def CustomerUploadResume(request):
    msg = ""
    status = 'Applied'
    if request.POST:
        cid = request.session['cust_id']
        jid = request.session["jid"]


        data = cust_reg.objects.get(cid=cid)

        job = AddJobs.objects.get(jobid=jid)

        if request.FILES.get("file"):
            myfile = request.FILES.get("file")
            if Jobapply.objects.filter(job_id=jid,cus_id=cid):
                msg="Already Uploaded"
                return render(request,'CustomerViewJob.html',{'msg':msg})
            else:
                insert=Jobapply.objects.create(job_id=jid,cus_id=cid,status=status,file=myfile,Cust_name=data.cname,Cust_phone=data.mobile,Cust_email=data.email,post=job.position)
                msg = "File Uploaded Successfully."
                return render(request,'CustomerViewJob.html',{'msg':msg})
    else:
        return render(request, "CustomerUploadResume.html", {"msg":msg})


def CustomerSearchTransportation(request):
    stations=Stationlist.objects.all()
    vehicle1=Vehicles.objects.all()
    if request.POST:
            di = request.POST.get('dist')
            station=di.replace(" ","")
            vehicle = request.POST.get('vehicle')
            str1 = di.replace(" ","")
            check=Transportation.objects.filter(station=station,capacity=vehicle)
            if check is None:
                return HttpResponse('fail')
            if check is not None:
                return render(request, "CustomerSearchTransportation.html",{'datas':check,"station": stations,"vehicle":vehicle1})

    else:
        return render(request, 'CustomerSearchTransportation.html', {"station": stations,"vehicle":vehicle1})


def CustomerBookTransport(request):

    taid = request.GET['id']
    request.session["taid"] = taid

    return redirect("/CustomerBookTransportation")


# Create your views here.

def CustomerBookTransportation(request):
    msg = ""
    cid = request.session['cust_id']
    taid = request.session['taid']
    da = datetime.date.today().strftime('%Y-%m-%d')
    status = 'Booked'
    if request.POST:

        cdate = request.POST.get("cdate")
        if cdate > da:
            Time = request.POST.get("Time")
            Destination = request.POST.get("Destination")
            date = request.POST.get("cdate")
            msg = "Your Booking Completed Successfully."
            insert=BookTransportations.objects.create(cid=cid,taid=taid,date=date,time=Time,destination=Destination,status=status)
            return render(request, "CustomerHome.html", {"msg": msg})
        else:
            msg="Please Enter A Valid Date"
            return render(request, "CustomerBookTransportation.html", {"msg": msg})
    else:
        return render(request, "CustomerBookTransportation.html", {"msg": msg})


def TransportationViewConfirmedBooking(request):
    data = ""
    da = datetime.date.today().strftime('%Y-%m-%d')
    tid = request.session['trnspt_id']
    select=BookTransportations.objects.filter(taid=tid,status='Accepted')
    return render(request, "TransportationViewConfirmedBooking.html", {"data": select})
from.models import Timming




def EmployeeAddTiming(request):
    msg = ""
    if request.POST:
        new=Timming.objects.all()
        if new is None:
            file = request.POST['Timing_file']
            current = date.today()
            insert = Timming.objects.create(Updated_Date=current, file=file)
            msg = "Timing Added Successfully"
        else:
            msg="Already added"
    return render(request, 'EmployeeAddTiming.html', {"msg": msg})

def AdminAddTiming(request):
    msg = ""
    if request.POST:
        new=Timming.objects.all()
        if new is None:
            file = request.POST['Timing_file']
            current = date.today()
            insert = Timming.objects.create(Updated_Date=current, file=file)
            msg = "Timing Added Successfully"
        else:
            msg="Already added"
    return render(request, 'AdminAddTiming.html', {"msg": msg})

def AdminTimingUpdate(request):
    msg = ""
    if request.POST:
        new=Timming.objects.all()
        if new is not None:
            file = request.POST['Timing_file']
            current = date.today()
            insert = Timming.objects.update(Updated_Date=current, file=file)
            msg = "Timing update Successfully"
        else:
            msg="Not Added yet"
    return render(request, 'EmployeeAddTiming.html', {"msg": msg})
def CustomerViewTiming(request):
    timming=Timming.objects.all()
    return render(request,'CustomerViewTiming.html',{'data':timming})

def logout(request):
    if 'usernameval' in request.session:
        del request.session['usernameval']
    return redirect('/')


def CancelBooking(request):
    id = request.GET.get('id')
    dele = BookTransportations.objects.get(bkid=id).delete()
    return redirect('/CustomerViewConfBooking')
