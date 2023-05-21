from django.db import models

# Create your models here.
class Proprietor(models.Model):
    PropID = models.CharField(max_length=10)
    PlotNumber = models.CharField(max_length = 5,null=True)
    PlotOwner = models.CharField(max_length=100,null=True)
    LicenseHolder = models.CharField(max_length = 100)
    ShopName = models.CharField(max_length=100,null=True)
    EmailID = models.EmailField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    AadharNumber = models.IntegerField()
    DateOfBirth=models.CharField(max_length=10)
    Aadtye=models.BooleanField()
    AClass=models.BooleanField()
    Processing=models.BooleanField()
    Hamal=models.BooleanField()
    RecordedBy = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.LicenseHolder
    
class InvoiceRecords(models.Model):
    IRProprietorID = models.CharField(max_length=10)
    IRLicenseHolderName = models.CharField(max_length=100)
    IRAadharNumber=models.IntegerField()
    IRDOB=models.CharField(max_length=10)
    IRDate = models.CharField(max_length=10)
    IRYear = models.CharField(max_length=10)
    IRLicenseFeesAadtye = models.IntegerField()
    IRLicenseFeesAClass = models.IntegerField()
    IRLicenseFeesProcessing = models.IntegerField()
    IRLicenseFeesHamal = models.IntegerField()
    IRLicenseRenewalFeesAadtye = models.IntegerField()
    IRLicenseRenewalFeesAClass = models.IntegerField()
    IRLicenseRenewalFeesProcessing = models.IntegerField()
    IRLicenseRenewalFeesHamal = models.IntegerField()
    IRPlotRent = models.IntegerField()
    IRMarketFeesMain = models.IntegerField()
    IRMarketFeesSecondary = models.IntegerField()
    IRSupervisionFees = models.IntegerField()
    IRFormFees = models.IntegerField()
    IRTavanPenalty = models.IntegerField()
    IRLateFees = models.IntegerField()
    IRLicenseFormFees = models.IntegerField()
    IRShoppingComplexRent = models.IntegerField()
    IRHishobPattiBook = models.IntegerField()
    IRBillBook = models.IntegerField()
    IRPohonchPavati = models.IntegerField()
    IROtherFees = models.IntegerField()
    IRNATax = models.IntegerField()
    IRTotalFees=models.IntegerField()
    IRCash = models.BooleanField()
    IRCheque = models.BooleanField()
    IRChequeNumber = models.CharField(max_length=25)
    IRUPI = models.BooleanField()
    IRTransactionNumber = models.CharField(max_length=50)
    IRRecordedBy = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.IRLicenseHolderName+", "+self.IRTransactionNumber

class Employee(models.Model):
    EmpName = models.CharField(max_length=50)
    EmpEmail = models.CharField(max_length=50)
    EmpPhone = models.CharField(max_length=10)
    EmpAadhar = models.IntegerField()
    EmpDesignation = models.CharField(max_length=15)
    EmpUsername = models.CharField(max_length=20)
    EmpPassword = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.EmpName