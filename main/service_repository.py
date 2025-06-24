from .models import PurchaseReport,WurthReport,McGrathReport,YhiaustraliaReport,RepcoReport
import pandas as pd


class PurchaseReportServices:
    def __init__(self):
        pass

    @staticmethod          
    def add_DataFrame_to_RepcoReport(df):
        filePath=df['filePath']
        supplier=df['supplier']
        maildate=df['maildate']
        part_number=df['part_number']
        description=df['description']
        uom=df['uom']
        retail_incl_gst=df['retail_incl_gst']
        unit_price_excl_gst=df['unit_price_excl_gst']
        qty_supplied=df['qty_supplied']
        total_gst=df['total_gst']
        s=df['s']
        total_incl_gst=df['total_incl_gst']
        for i in range(len(supplier)):
            report=RepcoReport(filePath=filePath[i],
                                  supplier=supplier[i],
                                  maildate=maildate[i],
                                  part_number=part_number[i],
                                  description=description[i],
                                  uom=uom[i],
                                  retail_incl_gst=retail_incl_gst[i],
                                  unit_price_excl_gst=unit_price_excl_gst[i],
                                  qty_supplied=qty_supplied[i],
                                  total_gst=total_gst[i],
                                  s=s[i],
                                  total_incl_gst=total_incl_gst[i]
                                )
            report.save()
    
    @staticmethod          
    def add_DataFrame_to_WurthReport(df):
        filePath=df['filePath']
        supplier=df['supplier']
        maildate=df['maildate']
        itemno=df['itemno']
        item_description=df['item_description']
        customer_part_no=df['customer_part_no']
        Ext_Net_Price_AUD= df['Ext_Net_Price_AUD']
        Price_Unit= df['Price_Unit']
        Price_AUD= df['Price_AUD']
        Quantity= df['Quantity']
        Pack_Unit= df['Pack_Unit']
        for i in range(len(supplier)):
            report=WurthReport(filePath=filePath[i],
                                  supplier=supplier[i],
                                  maildate=maildate[i],
                                  itemno=itemno[i],
                                  item_description=item_description[i],
                                  customer_part_no=customer_part_no[i],
                                  Ext_Net_Price_AUD=Ext_Net_Price_AUD[i],
                                  Price_Unit=Price_Unit[i],
                                  Price_AUD=Price_AUD[i],
                                  Quantity=Quantity[i],
                                  Pack_Unit=Pack_Unit[i]
                                )
            report.save()


    @staticmethod          
    def add_DataFrame_to_McGrathReport(df):
        filePath= df['filePath']
        supplier=df['supplier']
        maildate=df['maildate']
        location=df['location']
        part_Number= df['part_Number']
        description= df['description']
        ordered=df['ordered']
        supplied= df['supplied']
        unit_List= df['unit_List']
        unit_Net= df['unit_Net']
        GST_Code= df['GST_Code']
        total=df['total']
        for i in range(len(supplier)):
            report=McGrathReport(  
                    filePath= filePath[i],
                    supplier=supplier[i],
                    maildate=maildate[i],
                    location=location[i],
                    part_Number=part_Number[i],
                    description= description[i],
                    ordered=ordered[i],
                    supplied= supplied[i],
                    unit_List= unit_List[i],
                    unit_Net= unit_Net[i],
                    GST_Code= GST_Code[i],
                    total=total[i]
                    )
            report.save()
        print("add_DataFrame_to_McGrathReport saved!")

    @staticmethod          
    def add_DataFrame_to_YhiaustraliaReport(df):
        filePath=df['filePath']
        supplier=df['supplier']
        maildate=df['maildate']
        code= df['code']
        description= df['description']
        quantity=  df['quantity']
        unit_price=  df['unit_price']
        amount=  df['amount']
        for i in range(len(supplier)):
            report=YhiaustraliaReport(
                    filePath=filePath[i],
                    supplier=supplier[i],
                    maildate=maildate[i],
                    code= code[i],
                    description= description[i],
                    quantity= quantity[i],
                    unit_price= unit_price[i],
                    amount= amount[i]      
              )
            report.save()

    @staticmethod          
    def add_DataFrame_to_PurchaseReport(df):
        supplier=df['SUPPLIER']
        date=df['DATE']
        part_description=df['PART DESCRIPTION']
        part_number=df['PART NUMBER']
        trade_price=df['TRADE PRICE']
        total_count=df['TOTAL COUNT']
        purchase_count=df['PURCHASED COUNT']
        total_price=df['TOTAL PRICE']
        actual_price=df['ACTUAL PRICE']
        profit=df['PROFIT%']
        selling_price_exc_gst=df['SELLING PRICE(Exc.GST)']
        gst=df['GST']
        selling_price_inc_gst=df['SELLING PRICE(Inc.GST)']
        for i in range(len(supplier)):
            report=PurchaseReport(supplier=supplier[i],
                                  date=date[i],
                                  part_description=part_description[i],
                                  part_number=part_number[i],
                                  trade_price=trade_price[i],
                                  total_count=total_count[i],
                                  purchase_count=purchase_count[i],
                                  total_price=total_price[i],
                                  actual_price=actual_price[i],
                                  profit=profit[i],
                                  selling_price_exc_gst=selling_price_exc_gst[i],
                                  gst=gst[i],
                                  selling_price_inc_gst=selling_price_inc_gst[i]
                                  )
            report.save()
    
    @staticmethod
    def get_all_records_at_date(maildate):
        try:
            db = PurchaseReport.objects.filter(date=maildate)
            if not db.exists():
                print("No records found for the given date.")
        except Exception as e:
            print(f"Database error occurred: {e}")
        return db
    
    def addSinglePurchaseReport(self,df):
        pass

    def deletePurchaseReport(self,df):
        pass

    def updatePurchaseReport(self,df):
        pass

    def calculatePurchaseReport(self,df):
        pass


def updateWurthReport(report):
    try:
        wurth_report=WurthReport.objects.get(id=report['id'])
        print('wurth report loading')
        # wurth_report.filePath=report['filePath']
        # wurth_report.supplier=report['supplier']
        # wurth_report.maildate=report['maildate']
        wurth_report.itemno=report['itemno']
        wurth_report.item_description=report['item_description']
        wurth_report.customer_part_no=report['customer_part_no']
        wurth_report.Ext_Net_Price_AUD=report['Ext_Net_Price_AUD']
        wurth_report.Price_Unit=report['Price_Unit']
        wurth_report.Price_AUD=report['Price_AUD']
        wurth_report.Quantity=report['Quantity']
        wurth_report.Pack_Unit=report['Pack_Unit']
        wurth_report.save()
    except WurthReport.DoesNotExist:
        print("WurthReport not found.")



def updateMcGrathReport(report):
    try:
        McGrath_report=McGrathReport.objects.get(id=report['id'])
        # McGrath_report.filePath=report['filePath']
        # McGrath_report.supplier=report['supplier']
        # McGrath_report.maildate=report['maildate']
        McGrath_report.location=report['location']
        McGrath_report.part_Number=report['part_Number']
        McGrath_report.description=report['description']
        McGrath_report.ordered=report['ordered']
        McGrath_report.supplied=report['supplied']
        McGrath_report.unit_List=report['unit_List']
        McGrath_report.unit_Net=report['unit_Net']
        McGrath_report.GST_Code=report['GST_Code']
        McGrath_report.total=report['total']
        McGrath_report.save()
    except McGrathReport.DoesNotExist:
        print("McGrathReport not found.")


def updateYhiaustraliaReport(report):
    try:
        Yhi_Report=YhiaustraliaReport.objects.get(id=report['id'])
        # Yhi_Report.filePath=report['filePath']
        # Yhi_Report.supplier=report['supplier']
        # Yhi_Report.maildate=report['maildate']
        Yhi_Report.code=report['code']
        Yhi_Report.description=report['description']
        Yhi_Report.quantity=report['quantity']
        Yhi_Report.unit_price=report['unit_price']
        Yhi_Report.amount=report['amount']
        Yhi_Report.save()
    except YhiaustraliaReport.DoesNotExist:
        print("YhiaustraliaReport not found.")
