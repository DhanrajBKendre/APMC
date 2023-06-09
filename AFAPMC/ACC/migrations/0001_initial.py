# Generated by Django 4.1.4 on 2023-05-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("EmpName", models.CharField(max_length=50)),
                ("EmpEmail", models.CharField(max_length=50)),
                ("EmpPhone", models.CharField(max_length=10)),
                ("EmpAadhar", models.IntegerField()),
                ("EmpDesignation", models.CharField(max_length=15)),
                ("EmpUsername", models.CharField(max_length=20)),
                ("EmpPassword", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceRecords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("IRProprietorID", models.CharField(max_length=10)),
                ("IRLicenseHolderName", models.CharField(max_length=100)),
                ("IRAadharNumber", models.IntegerField()),
                ("IRDOB", models.CharField(max_length=10)),
                ("IRDate", models.CharField(max_length=10)),
                ("IRYear", models.CharField(max_length=10)),
                ("IRLicenseFeesAadtye", models.IntegerField()),
                ("IRLicenseFeesAClass", models.IntegerField()),
                ("IRLicenseFeesProcessing", models.IntegerField()),
                ("IRLicenseFeesHamal", models.IntegerField()),
                ("IRLicenseRenewalFeesAadtye", models.IntegerField()),
                ("IRLicenseRenewalFeesAClass", models.IntegerField()),
                ("IRLicenseRenewalFeesProcessing", models.IntegerField()),
                ("IRLicenseRenewalFeesHamal", models.IntegerField()),
                ("IRPlotRent", models.IntegerField()),
                ("IRMarketFeesMain", models.IntegerField()),
                ("IRMarketFeesSecondary", models.IntegerField()),
                ("IRSupervisionFees", models.IntegerField()),
                ("IRFormFees", models.IntegerField()),
                ("IRTavanPenalty", models.IntegerField()),
                ("IRLateFees", models.IntegerField()),
                ("IRLicenseFormFees", models.IntegerField()),
                ("IRShoppingComplexRent", models.IntegerField()),
                ("IRHishobPattiBook", models.IntegerField()),
                ("IRBillBook", models.IntegerField()),
                ("IRPohonchPavati", models.IntegerField()),
                ("IROtherFees", models.IntegerField()),
                ("IRNATax", models.IntegerField()),
                ("IRTotalFees", models.IntegerField()),
                ("IRCash", models.BooleanField()),
                ("IRCheque", models.BooleanField()),
                ("IRChequeNumber", models.CharField(max_length=25)),
                ("IRUPI", models.BooleanField()),
                ("IRTransactionNumber", models.CharField(max_length=50)),
                ("IRRecordedBy", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Proprietor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("PropID", models.CharField(max_length=10)),
                ("PlotNumber", models.CharField(max_length=5, null=True)),
                ("PlotOwner", models.CharField(max_length=100, null=True)),
                ("LicenseHolder", models.CharField(max_length=100)),
                ("ShopName", models.CharField(max_length=100, null=True)),
                ("EmailID", models.EmailField(max_length=100)),
                ("PhoneNumber", models.CharField(max_length=10)),
                ("AadharNumber", models.IntegerField()),
                ("DateOfBirth", models.CharField(max_length=10)),
                ("Aadtye", models.BooleanField()),
                ("AClass", models.BooleanField()),
                ("Processing", models.BooleanField()),
                ("Hamal", models.BooleanField()),
                ("RecordedBy", models.CharField(max_length=25)),
            ],
        ),
    ]
