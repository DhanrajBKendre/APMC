from django.db.models import Count
from django.db.models import Sum
import pandas as pd
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ACC.models import Proprietor
from ACC.models import InvoiceRecords
from ACC.models import Employee
from django.db.models import Q
from datetime import datetime
from datetime import date
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

#INDEX PAGE
@login_required(login_url = '/login')
def index(request):
    try:
        if request.user.is_anonymous:
            return redirect('/login')
        else:
            return render(request, 'html/index.html')
    except:
        return render(request, 'html/pagenotfound.html')

#LOGIN PAGE
def loginUser(request):
    if request.method == "POST":
        usern = request.POST['username']
        userp = request.POST['password']
        user = authenticate(request, username=usern, password=userp)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'html/login.html')
    return render(request, "html/login.html")

#LOGOUT
def logoutUser(request):
    logout(request)
    return redirect('/login')

#ADD EMPLOYEE PAGE
def signup(request):
    if request.method == "POST":
        aename = request.POST.get('name')
        aeemail = request.POST.get('email')
        aephone = request.POST.get('mobileno')
        if request.POST.get('aadhar')=="":
            aeaadhar = 000000000000
        else:
            aeaadhar = request.POST.get('aadhar')
        aedesig = request.POST.get('designation')
        namelist = aename.split(" ")
        usernamestring = namelist[0]+namelist[1][0]+namelist[2][0]
        olist = [aeemail, aephone, aeaadhar, aedesig]
        namelist.extend(olist)
        passwordstring = ""
        for i in {i[0] for i in namelist}:
            passwordstring = passwordstring+i[0]
        aeusername = usernamestring
        aepassword = passwordstring
        del namelist, olist, usernamestring, passwordstring
        emp = Employee.objects.create(EmpName=aename, EmpEmail=aeemail, EmpPhone=aephone,EmpAadhar=aeaadhar, EmpDesignation=aedesig, EmpUsername=aeusername, EmpPassword=aepassword)
        emp.save()
        if aedesig == "Secretary":
            user = User.objects.create_superuser(username=aeusername,email=aeemail,password=aepassword)
        else:
            user = User.objects.create_user(username=aeusername, email=aeemail, password=aepassword)
        user.save()
        messages.success(
            request, f'Employee Record Added With Username: {aeusername} and Password: {aepassword}')
    return render(request, 'html/signup.html')

#REPORTS PAGE
@login_required(login_url='/login')
def reports(request):
    return render(request, 'html/reports.html')

#ADD PROPRIETOR PAGE
@login_required(login_url='/login')
def addproprietor(request):
    try:
        csuser = str(request.user)
        if request.method == "POST":
            applotnumber = request.POST.get('plotnumber')
            applotowner = request.POST.get('plotowner')
            aplicenseholder = request.POST.get('licenseholder')
            apshopname = request.POST.get('shopname')
            apemail = request.POST.get('emailid')
            apphone = request.POST.get('phonenumber')
            if request.POST.get('aadharnumber')=="":
                apaadhar = 000000000000
            else:
                apaadhar = int(request.POST.get('aadharnumber'))
            apdob = request.POST.get('dateofbirth')
            apaadtye = bool(request.POST.get('aadtye', ""))
            apaclass = bool(request.POST.get('aclass', ""))
            approcessing = bool(request.POST.get('processing', ""))
            aphamal = bool(request.POST.get('hamal', ""))
            proprietorlist = Proprietor.objects.create(PlotNumber=applotnumber, PlotOwner=applotowner, LicenseHolder=aplicenseholder, ShopName=apshopname, EmailID=apemail,PhoneNumber=apphone, AadharNumber=apaadhar, DateOfBirth=apdob, Aadtye=apaadtye, AClass=apaclass, Processing=approcessing, Hamal=aphamal, RecordedBy=csuser)
            proprietorlist.save()
            if len(str(proprietorlist.id)) == 1:
                proprietorlist.PropID = "APMC00"+str(proprietorlist.id)
            elif len(str(proprietorlist.id)) == 2:
                proprietorlist.PropID = "APMC0"+str(proprietorlist.id)
            else:
                proprietorlist.PropID = "APMC"+str(proprietorlist.id)
            proprietorlist.save()
            messages.success(
                request, f'Proprietor Record Added Sucessfully With PropID: {proprietorlist.PropID}')
    except Exception as f:
        messages.error(request, f)
    return render(request, 'html/addproprietor.html')

#SEARCH PROPRIETOR
@login_required(login_url='/login')
def searchproprietor(request):
    searchq = request.POST.get('searchproprietorsearchbox')
    searchr = Proprietor.objects.filter(LicenseHolder__iexact=searchq)
    try:
        if request.method == "POST":
            print(searchr)
    except Exception as e:
        messages.error(request, e)
    return render(request, 'html/searchproprietor.html', {'data': searchr})

#UPDATE PROPRIETOR
@login_required(login_url='/login')
def updateproprietor(request, i_id):
    i = get_object_or_404(Proprietor, pk=i_id)
    csuser = str(request.user)
    try:
        if request.method == "POST":
            i.PlotNumber = request.POST.get('upplotnumber')
            i.PlotOwner = request.POST.get('upplotowner')
            i.LicenseHolder = request.POST.get('uplicenseholder')
            i.ShopName = request.POST.get('upshopname')
            i.EmailID = request.POST.get('upemailid')
            i.PhoneNumber = request.POST.get('upphonenumber')
            if request.POST.get('upaadharnumber')=="":
                i.AadharNumber = 000000000000
            else:
                i.AadharNumber = int(request.POST.get('upaadharnumber'))
            i.DateOfBirth = request.POST.get('dateofbirth')
            i.Aadtye = bool(request.POST.get('upaadtye', ""))
            i.AClass = bool(request.POST.get('upaclass', ""))
            i.Processing = bool(request.POST.get('upprocessing', ""))
            i.Hamal = bool(request.POST.get('uphamal', ""))
            i.RecordedBy = csuser
            i.save()
            messages.success(request, 'Proprietor Record Updated Sucessfully!')
    except Exception as e:
        messages.error(request, e)
    return render(request, 'html/updateproprietor.html', {'i': i})

#DELETE PROPRIETOR
@login_required(login_url='/login')
def deleteproprietor(request, i_id):
    i = get_object_or_404(Proprietor, pk=i_id)
    try:
        if request.method == "POST":
            i.delete()
            messages.success(
                request, 'Proprietor Record Deleted Successfully As Below!')
    except Exception as e:
        messages.error(request, e)
    return render(request, 'html/deleteproprietor.html', {'i': i})

#CREATE INVOICE
@login_required(login_url='/login')
def createinvoice(request, i_id):
    i = get_object_or_404(Proprietor, pk=i_id)
    csuser = str(request.user)
    pyear = datetime.now().year
    cyear = datetime.now().year+1
    today = datetime.today().strftime("%Y-%m-%d")
    if request.method == "POST":
        ciproprietorid = i.PropID
        cilicenseholdername = i.LicenseHolder
        ciadharnumber = i.AadharNumber
        cidob = i.DateOfBirth
        cidate = today
        ciyear = str(pyear)+"-"+str(cyear)
        if request.POST.get('cilicensefeesaadtye') == "":
            cilicensefeesaadtye = 0
        else:
            cilicensefeesaadtye = int(request.POST.get('cilicensefeesaadtye'))
        if request.POST.get('cilicensefeesaclass') == "":
            cilicensefeesaclass = 0
        else:
            cilicensefeesaclass = int(request.POST.get('cilicensefeesaclass'))
        if request.POST.get('cilicensefeesprocessing') == "":
            cilicensefeesprocessing = 0
        else:
            cilicensefeesprocessing = int(
                request.POST.get('cilicensefeesprocessing'))
        if request.POST.get('cilicensefeeshamal') == "":
            cilicensefeeshamal = 0
        else:
            cilicensefeeshamal = int(request.POST.get('cilicensefeeshamal'))
        if request.POST.get('cilicenserenewalfeesaadtye') == "":
            cilicenserenewalfeesaadtye = 0
        else:
            cilicenserenewalfeesaadtye = int(
                request.POST.get('cilicenserenewalfeesaadtye'))
        if request.POST.get('cilicenserenewalfeesaclass') == "":
            cilicenserenewalfeesaclass = 0
        else:
            cilicenserenewalfeesaclass = int(
                request.POST.get('cilicenserenewalfeesaclass'))
        if request.POST.get('cilicenserenewalfeesprocessing') == "":
            cilicenserenewalfeesprocessing = 0
        else:
            cilicenserenewalfeesprocessing = int(
                request.POST.get('cilicenserenewalfeesprocessing'))
        if request.POST.get('cilicenserenewalfeeshamal') == "":
            cilicenserenewalfeeshamal = 0
        else:
            cilicenserenewalfeeshamal = int(
                request.POST.get('cilicenserenewalfeeshamal'))
        if request.POST.get('ciplotrent') == "":
            ciplotrent = 0
        else:
            ciplotrent = int(request.POST.get('ciplotrent'))
        if request.POST.get('cimarketfeesmain') == "":
            cimarketfeesmain = 0
        else:
            cimarketfeesmain = int(request.POST.get('cimarketfeesmain'))
        if request.POST.get('cimarketfeessecondary') == "":
            cimarketfeessecondary = 0
        else:
            cimarketfeessecondary = int(
                request.POST.get('cimarketfeessecondary'))
        if request.POST.get('cisupervisionfees') == "":
            cisupervisionfees = 0
        else:
            cisupervisionfees = int(request.POST.get('cisupervisionfees'))
        if request.POST.get('ciformfees') == "":
            ciformfees = 0
        else:
            ciformfees = int(request.POST.get('ciformfees'))
        if request.POST.get('citavanpenalty') == "":
            citavanpenalty = 0
        else:
            citavanpenalty = int(request.POST.get('citavanpenalty'))
        if request.POST.get('cilatefees') == "":
            cilatefees = 0
        else:
            cilatefees = int(request.POST.get('cilatefees'))
        if request.POST.get('cilicenseformfees') == "":
            cilicenseformfees = 0
        else:
            cilicenseformfees = int(request.POST.get('cilicenseformfees'))
        if request.POST.get('cishoppingcomplexrent') == "":
            cishoppingcomplexrent = 0
        else:
            cishoppingcomplexrent = int(request.POST.get('cishoppingcomplexrent'))
        if request.POST.get('cihishobpattibook')=="":
            cihishobpattibook=0
        else:
            cihishobpattibook = int(request.POST.get('cihishobpattibook'))
        if request.POST.get('cibillbook')=="":
            cibillbook=0
        else:
            cibillbook = int(request.POST.get('cibillbook'))
        if request.POST.get('cipohonchpavati')=="":
            cipohonchpavati=0
        else:
            cipohonchpavati = int(request.POST.get('cipohonchpavati'))
        if request.POST.get('ciotherfees')=="":
            ciotherfees=0
        else:
            ciotherfees = int(request.POST.get('ciotherfees'))
        if request.POST.get('cinatax')=="":
            cinatax=0
        else:
            cinatax = int(request.POST.get('cinatax'))
        if request.POST.get('citotalfees')=="":
            citotalfees=0
        else:
            citotalfees = int(request.POST.get('citotalfees'))
        cicash = bool(request.POST.get('cicash', ""))
        cicheque = bool(request.POST.get('cicheque', ""))
        cichequenumber = request.POST.get('cichequenumber')
        ciupi = bool(request.POST.get('ciupi', ""))
        citransactionnumber = str(i.PropID)+"TXN" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
        cirecordedby = csuser
        invoicelist = InvoiceRecords.objects.create(IRProprietorID=ciproprietorid, IRLicenseHolderName=cilicenseholdername, IRAadharNumber=ciadharnumber, IRDOB=cidob, IRDate=cidate, IRYear=ciyear, IRLicenseFeesAadtye=cilicensefeesaadtye, IRLicenseFeesAClass=cilicensefeesaclass, IRLicenseFeesProcessing=cilicensefeesprocessing, IRLicenseFeesHamal=cilicensefeeshamal, IRLicenseRenewalFeesAadtye=cilicenserenewalfeesaadtye, IRLicenseRenewalFeesAClass=cilicenserenewalfeesaclass, IRLicenseRenewalFeesProcessing=cilicenserenewalfeesprocessing, IRLicenseRenewalFeesHamal=cilicenserenewalfeeshamal, IRPlotRent=ciplotrent,IRMarketFeesMain=cimarketfeesmain, IRMarketFeesSecondary=cimarketfeessecondary, IRSupervisionFees=cisupervisionfees, IRFormFees=ciformfees, IRTavanPenalty=citavanpenalty, IRLateFees=cilatefees, IRLicenseFormFees=cilicenseformfees, IRShoppingComplexRent=cishoppingcomplexrent, IRHishobPattiBook=cihishobpattibook, IRBillBook=cibillbook, IRPohonchPavati=cipohonchpavati, IROtherFees=ciotherfees, IRNATax=cinatax, IRTotalFees=citotalfees, IRCash=cicash, IRCheque=cicheque, IRChequeNumber=cichequenumber, IRUPI=ciupi, IRTransactionNumber=citransactionnumber, IRRecordedBy=cirecordedby)
        invoicelist.save()
        messages.success(request, f'Receipt Record Saved Sucessfully With Transaction Number: {citransactionnumber}')
        return render(request, 'html/error.html')
    return render(request, 'html/createinvoice.html', {'i': i, "pyear": pyear, "cyear": cyear, "today": today})

#REDIRECING PAGES
@login_required(login_url='/login')
def error(request):
    return render(request, 'html/error.html')

#UPDATE PROPRIETOR PAGE WITHOUT DATA
@login_required(login_url='/login')
def upp(request):
    return render(request, 'html/error.html')

#DELETE PROPRIETOR PAGE WITHOUT DATA
@login_required(login_url='/login')
def dpp(request):
    return render(request, 'html/error.html')

#CREATE INVOICE PAGE WITHOUT DATA
@login_required(login_url='/login')
def ci(request):
    return render(request, 'html/error.html')

#INVOICE RECORDS REPORT PAGE
@login_required(login_url='/login')
def invoicerecords(request):
    irl = get_list_or_404(InvoiceRecords)
    return render(request, 'html/invoicerecords.html', {'invoicelist': irl})

#PROPRIETOR LIST REPORT PAGE
@login_required(login_url='/login')
def proprecords(request):
    prl = get_list_or_404(Proprietor)
    return render(request, 'html/proprietors.html', {'prprecords': prl})

#FINANCIAL ASPECT REPORT PAGE
@login_required(login_url='/login')
def financerecords(request):
    if request.method == "POST":
        fiviewstartdate = request.POST.get('startdate')
        if fiviewstartdate == "":
            fiviewstartdate = "2023-04-01"
        fiviewenddate = request.POST.get('enddate')
        if fiviewenddate == "":
            fiviewenddate = "2024-03-31"
        sdate = datetime.strptime(
            fiviewstartdate, "%Y-%m-%d")-timedelta(days=1)
        edate = datetime.strptime(fiviewenddate, "%Y-%m-%d")+timedelta(days=1)
        fiviewlicenseholder = request.POST.get('filicenseholder')
        fiviewselectoption = request.POST.getlist('selectoption')
        fiviewrecordedby = request.POST.get('firecordedby')
        fiviewaadhar = request.POST.get('fiaadhar')
        # SEARCHING BY AADHAR NUMBER
        if fiviewselectoption[0] == "Aadhar Number" and len(fiviewselectoption) == 1:
            mydata = InvoiceRecords.objects.filter(IRAadharNumber=fiviewaadhar)
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY NAME OF LICENSE HOLDER
        elif fiviewselectoption[0] == "License Holder" and len(fiviewselectoption) == 1:
            mydata = InvoiceRecords.objects.filter(
                IRLicenseHolderName__iexact=fiviewlicenseholder)
            return render(request, 'html/finance.html', {'financetable': mydata})
        # #SEARCHING BY NAME OF USER WHO RECORDED THE TRANSACTIONS
        elif fiviewselectoption[0] == "Recorded By" and len(fiviewselectoption) == 1:
            mydata = InvoiceRecords.objects.filter(
                IRRecordedBy__iexact=fiviewrecordedby)
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY THE START DATE AND END DATE
        elif fiviewselectoption[0] == "Date" and len(fiviewselectoption) == 1:
            mydata = InvoiceRecords.objects.filter(
                IRDate__gte=sdate, IRDate__lte=edate)
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY THE NAME OF LICENSE HOLDER AND DATE
        elif fiviewselectoption[0] == "Date" and fiviewselectoption[1] == "License Holder" and len(fiviewselectoption) == 2:
            mydata = InvoiceRecords.objects.filter(Q(IRDate__gte=sdate) & Q(IRDate__lte=edate) & Q(IRLicenseHolderName=fiviewlicenseholder))
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY THE NAME OF LICENSE HOLDER AND RECORDED BY
        elif fiviewselectoption[0] == "License Holder" and fiviewselectoption[1] == "Recorded By" and len(fiviewselectoption) == 2:
            mydata = InvoiceRecords.objects.filter(Q(IRRecordedBy__iexact=fiviewrecordedby) & Q(IRLicenseHolderName__iexact=fiviewlicenseholder))
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY THE NAME OF DATE AND RECORDED BY
        elif fiviewselectoption[0] == "Date" and fiviewselectoption[1] == "Recorded By" and len(fiviewselectoption) == 2:
            mydata = InvoiceRecords.objects.filter(Q(IRDate__gte=sdate) & Q(IRDate__lte=edate) & Q(IRRecordedBy__iexact=fiviewrecordedby))
            return render(request, 'html/finance.html', {'financetable': mydata})
        # SEARCHING BY THE NAME OF DATE AND NAME OF LICENSE HOLDER AND RECORDED BY
        elif fiviewselectoption[0] == "Date" and fiviewselectoption[1] == "License Holder" and fiviewselectoption[2] == "Recorded By" and len(fiviewselectoption) == 3:
            mydata = InvoiceRecords.objects.filter(Q(IRDate__gte=sdate) & Q(IRDate__lte=edate) & Q(IRLicenseHolderName__iexact=fiviewlicenseholder) & Q(IRRecordedBy__iexact=fiviewrecordedby))
            return render(request, 'html/finance.html', {'financetable': mydata})
        else:
            mydata = InvoiceRecords.objects.all()
            return render(request,'html/finance.html',{'financetable':mydata})
    return render(request, 'html/finance.html')


#TALLY REPORT PAGE
@login_required(login_url='/login')
def tally(request):
    mydata = InvoiceRecords.objects.all().values()
    df = pd.DataFrame(mydata)
    resdf = pd.DataFrame(df.groupby('IRLicenseHolderName')[['IRLicenseFeesAadtye','IRLicenseFeesAClass','IRLicenseFeesProcessing','IRLicenseFeesHamal','IRLicenseRenewalFeesAadtye','IRLicenseRenewalFeesAClass','IRLicenseRenewalFeesProcessing','IRLicenseRenewalFeesHamal','IRPlotRent','IRMarketFeesMain','IRMarketFeesSecondary','IRSupervisionFees','IRFormFees','IRTavanPenalty','IRLateFees','IRLicenseFormFees','IRShoppingComplexRent','IRHishobPattiBook','IRBillBook','IRPohonchPavati','IROtherFees','IRNATax','IRTotalFees']].sum())
    mydict = {
        'resdf': resdf.to_records()
    }
    return render(request, 'html/tally.html', context=mydict)