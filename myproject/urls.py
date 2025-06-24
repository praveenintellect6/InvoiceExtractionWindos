"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

urlpatterns = [
    path('.well-known/appspecific/com.chrome.devtools.json', lambda r: JsonResponse({}, status=204)),
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # path('upload_pdf/',views.upload_pdf,name='upload_pdf'),
    # path('scrap_pdf/',views.scrap_pdf,name='scrap_pdf'),
    path('collect_mail_invoice/',views.collect_mail_invoice,name='collect_mail_invoice'),
    path('show_mail_dates/',views.show_mail_dates,name='show_mail_dates'),
    path('open_data_sheet/<str:urldata>/',views.open_data_sheet,name='open_data_sheet'),
    path('update_report/',views.update_report,name='update_report'),
    path('settingsview/',views.settingsview,name='settingsview'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('get_suppliers/',views.get_suppliers,name='get_suppliers'),
    path('get_suppliers_column_map/',views.get_suppliers_column_map,name="get_suppliers_column_map"),
    path('get_suppliers_headers/',views.get_suppliers_headers,name="get_suppliers_headers"),
    path('create_column_mapping/',views.create_column_mapping,name="create_column_mapping"),
    path('reportview/',views.reporview,name="reportview"),
    path('save-record/', views.save_record, name='save_record'),
    path('delete-record/', views.delete_record, name='delete_record'),
    path('generate_report_reportview/',views.generate_report_reportview,name='generate_report_reportview'),
    path('showcases',views.showcases,name="showcases"),
    path('add_case_data',views.add_case_data,name="add_case_data"),
    path('get_suppliers_headers_value',views.get_suppliers_headers_value,name="get_suppliers_headers_value"),
    path('delete_case',views.delete_case,name="delete_case"),
    path('generated_report',views.generated_report,name="generated_report"),
    path('show_mail_dates_report/',views.show_mail_dates_report,name="show_mail_dates_report"),
    path('generate_p_reportview/',views.generate_p_reportview,name="generate_p_reportview"),
    path('upload_excel/',views.upload_excel,name="upload_excel"),
    path('convert_to_report/',views.convert_to_report,name="convert_to_report"),
    path('make_all_preport/',views.make_all_preport,name='make_all_preport'),
    path('delete_mailed_records/',views.delete_mailed_records,name="delete_mailed_records"),
    path('filecorrection/',views.filecorrection,name="filecorrection"),
    path('showunseen_mails/', views.showunseen_mails, name="showunseen_mails"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)