from awd_main.celery import app
import time
from django.core.management import call_command
from .utils import send_email_notification,generate_csv_file
from django.conf import settings

@app.task
def celery_test_task():
    print('test1')
    time.sleep(5)
    mail_subject = 'Test subject'
    message = 'This is a Test Email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'Email sent successfully.'
    
@app.task
def import_data_task(file_path,model_name):
    try:
        call_command('importdata',file_path,model_name)
    except Exception as e:
        raise e
    mail_subject = 'Import data completed'
    message = 'your data import has been successfull'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'Data imported successfully' 

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata',model_name)
    except Exception as e:
        raise e
    file_path = generate_csv_file(model_name)
    mail_subject = 'Export data completed'
    message = 'your data export has been successfull,please find an attachment'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email,attachment=file_path)
    return 'Data exported successfully'