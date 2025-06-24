from django.apps import AppConfig
import logging
from django.conf import settings
import os
from datetime import date,datetime
from django.core.cache import cache
import threading
import time
import requests
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    def ready(self):
      if os.environ.get('RUN_MAIN') != 'true':
          return
      from .models import WurthReport, McGrathReport, YhiaustraliaReport
      cache.set('report_num_columns',['trade_price','total_count','purchase_count','total_price','actual_price','profit',
                                      'selling_price_exc_gst','gst','selling_price_inc_gst',],timeout=None)
      cache.set('supplier_table_name',{"wurth": [field.name for field in WurthReport._meta.get_fields() if not field.many_to_many and not field.one_to_many],
                                      "YHI AUSTRALIA": [field.name for field in YhiaustraliaReport._meta.get_fields() if not field.many_to_many and not field.one_to_many],
                                      "John_McGrath":[field.name for field in McGrathReport._meta.get_fields() if not field.many_to_many and not field.one_to_many]
                                      },
                                      timeout=None)
      cache.set('suppliertable_modelname',{"wurth":"WurthReport","YHI AUSTRALIA":"YhiaustraliaReport","John_McGrath":"McGrathReport"},timeout=None)
      cache.set('invoicelist',[])
      cache.set('invoicelist_date','')
      from .utils import MailAutomationClass,UtilityClasses
      from .service_repository import PurchaseReportServices
      from .models import PurchaseReport
      if settings.SCHEDULER_AUTOSTART:
            scheduler = BackgroundScheduler()
            scheduler.add_job( MailAutomationClass.mail_unseen_task, 'interval', seconds=5)
            scheduler.start()

    #   def backgroundtask():
    #       count=0
    #       subject={}
    #       filenames=[]
    #       while True:
    #           print("task running....")
    #           MailAutomationClass.mail_unseen_task()
    #           # status,mail_subject,folder_date_path,attachment,filecount=MailAutomationClass.fetch_emails_cron_task(date.today())
    #           # basepath=os.path.join('media',"in_invoice",date.today().strftime("%Y-%m-%d"))
    #           # os.makedirs(basepath,exist_ok=True)
    #           # if count<filecount:
    #           #       filenames=list(mail_subject.keys()-subject.keys())
    #           #       dfsets=[]
    #           #       for i in filenames:
    #           #           fname=os.path.join(basepath,i)
    #           #           dfsets.append(UtilityClasses.scrap(fname,date.today().strftime('%Y-%m-%d'),mail_subject))
    #           #           MailAutomationClass.send_mail(to_email="praveengopi998@gmail.com",subject=f"Invoice Alert {datetime.now()}",body=f"New Invoice Received {i}")
    #           #           sheets = pd.read_excel(fname)
    #           #           if sheets['supplier'].iloc[0]=="wurth":
    #           #               PurchaseReportServices.add_DataFrame_to_WurthReport(sheets)
    #           #           elif sheets['supplier'].iloc[0]=="John_McGrath":
    #           #               PurchaseReportServices.add_DataFrame_to_McGrathReport(sheets)
    #           #           elif sheets['supplier'].iloc[0]=="YHI AUSTRALIA":
    #           #               PurchaseReportServices.add_DataFrame_to_YhiaustraliaReport(sheets)
    #           #       queryset=PurchaseReport.objects.filter(date=cache.get("invoicelist_date")).values()
    #           #       df = pd.DataFrame(list(queryset))
    #           #       file_excel_path=f"media/PurchaseReport_{date.today().strftime('%Y-%m-%d')}.xlsx"
    #           #       df.to_excel(file_excel_path, index=False)
    #           #       count=filecount
    #           # print("status:",status)
    #           # print("mail_subject:",mail_subject)
    #           # print("folder_date_path",folder_date_path)
    #           # print("attachments",attachments)
    #           # pdf_files = [os.path.join(folder_date_path,f)  for f in os.listdir(folder_date_path) if os.path.isfile(os.path.join(folder_date_path, f)) and f.lower().endswith('.pdf')]
    #           # dfsets=[]
    #           time.sleep(3) 
    #   t=threading.Thread(target=backgroundtask,daemon=True)
    #   t.start()
