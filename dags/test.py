from data_tools.api.email.gmail import send_gmail

def send_mail():
    receiver = 'noufal85@gmail.com'
    subject = 'testing DAG'
    body ="ignore"
    smtp = "edappa1985@gmail.com"
    send_gmail(receiver,subject,body,smtp,attachment=None)



if __name__ =="__main__":
    send_mail()