import win32com.client


def send_outlook_email(subject, body, to_email):
    #launch outlook
    outlook= win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject  = subject
    mail.Body = body
    mail.To = to_email
    mail.Send()

send_outlook_email("hello - today","HI testing","gayathri.be2011@gmail.com")