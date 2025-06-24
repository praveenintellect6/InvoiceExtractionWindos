from django.db import models

class RepcoReport(models.Model):
    filePath=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    maildate=models.CharField(max_length=100)
    part_number= models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    uom=models.CharField(max_length=50)
    retail_incl_gst=models.CharField(max_length=10)
    unit_price_excl_gst=models.CharField(max_length=10)
    qty_supplied=models.CharField(max_length=10)
    total_gst=models.CharField(max_length=10)
    s=models.CharField(max_length=10)
    total_incl_gst=models.CharField(max_length=10)

class WurthReport(models.Model):
    filePath=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    maildate=models.CharField(max_length=100)
    itemno= models.CharField(max_length=100)
    item_description=models.CharField(max_length=255)
    customer_part_no=models.CharField(max_length=100)
    Ext_Net_Price_AUD= models.CharField(max_length=10)
    Price_Unit= models.CharField(max_length=10)
    Price_AUD= models.CharField(max_length=10)
    Quantity= models.CharField(max_length=10)
    Pack_Unit= models.CharField(max_length=10)


class McGrathReport(models.Model):
    filePath=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    maildate=models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    part_Number= models.CharField(max_length=100)
    description= models.CharField(max_length=255)
    ordered= models.CharField(max_length=10)
    supplied= models.CharField(max_length=10)
    unit_List= models.CharField(max_length=10)
    unit_Net= models.CharField(max_length=10)
    GST_Code= models.CharField(max_length=10)
    total= models.CharField(max_length=10)


class YhiaustraliaReport(models.Model):
    filePath=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    maildate=models.CharField(max_length=100)
    code= models.CharField(max_length=100)
    description= models.CharField(max_length=255)
    quantity=  models.CharField(max_length=10)
    unit_price=  models.CharField(max_length=10)
    amount=  models.CharField(max_length=10)


class PurchaseReport(models.Model):
    #pdf_url=models.CharField(max_length=255)
    supplier=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    part_description=models.CharField(max_length=255)
    part_number=models.CharField(max_length=100)
    trade_price=models.CharField(max_length=10)
    total_count=models.CharField(max_length=10)
    purchase_count=models.CharField(max_length=10)
    total_price=models.CharField(max_length=10)
    actual_price=models.CharField(max_length=10)
    profit=models.CharField(max_length=10)
    selling_price_exc_gst=models.CharField(max_length=10)
    gst=models.CharField(max_length=10)
    selling_price_inc_gst=models.CharField(max_length=10)
    class Meta:
        db_table= 'purchasereport'
        

class InvoiceInfo(models.Model):
    mailsubject = models.CharField(max_length=255, unique=True)
    maildate = models.CharField(max_length=100)
    supplier = models.CharField(max_length=255, unique=True)
    ou_invoice_url = models.CharField(max_length=255, unique=True)
    in_invoice_url = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table= 'invoiceinfo'


class Supplier(models.Model):
    supplier_name=models.CharField(max_length=100,unique=True)


class CaseModel(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    minvalue=models.IntegerField()
    maxvalue=models.IntegerField()
    actual_price=models.CharField(max_length=100)
    profit=models.CharField(max_length=150)
    selling_price_exc_gst=models.CharField(max_length=150)
    gst=models.CharField(max_length=150)
    selling_price_inc_gst=models.CharField(max_length=150)


class ColumnMapping(models.Model):
    supplier_col=models.CharField(max_length=100,unique=True)
    date_col=models.CharField(max_length=100)
    part_description_col=models.CharField(max_length=100)
    part_number_col=models.CharField(max_length=100)
    trade_price_col=models.CharField(max_length=100)
    total_count_col=models.CharField(max_length=100)
    purchase_count_col=models.CharField(max_length=100)
    total_price_col=models.CharField(max_length=100)
    actual_price_col=models.CharField(max_length=100)
    profit_col=models.CharField(max_length=100)
    selling_price_exc_gst_col=models.CharField(max_length=100)
    gst_col=models.CharField(max_length=100)
    selling_price_inc_gst_col=models.CharField(max_length=100)


class ScrappedDate(models.Model):
    maildate=models.DateField()


class DataDownloaded_Date(models.Model):
    maildate=models.DateField()







