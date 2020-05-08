from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


from data_tools.api.email.gmail import send_gmail

def send_mail():
    receiver = 'noufal85@gmail.com'
    subject = 'testing DAG'
    body ="ignore"
    smtp = "edappa1985@gmail.com"
    send_gmail(receiver,subject,body,smtp,attachment=None)

yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2020, 5, 8),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('store_dag',default_args=default_args,schedule_interval='@daily', template_searchpath=['/usr/local/airflow/sql_files'], catchup=False) as dag:

    #t1=BashOperator(task_id='check_file_exists', bash_command='shasum ~/store_files_airflow/raw_store_transactions.csv', retries=2, retry_delay=timedelta(seconds=15))

    t1 = PythonOperator(task_id='email', python_callable=send_mail)

    t2 = PythonOperator(task_id='email2', python_callable=send_mail)

    t1>>t2

   