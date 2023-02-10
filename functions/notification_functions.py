import subprocess
import smtplib

# TODO: embbed the variable in the applescript to get this working
# def popup(text:str):
#     applescript = """
#     display dialog {"i"} ¬
#     with title "Your answer" ¬
#     with icon caution ¬
#     buttons {"OK"}
#     """
#     # display the text as dialog
#     # applescript = "display dialog {'"+text+"'} with title 'Your answer' with icon caution buttons {'OK'}"
#     subprocess.call("osascript -e '{}'".format(applescript), shell=True)


def send_email(sender, recipient, subject, message, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(sender, recipient, message)
        server.quit()
        print("Successfully sent email")
    except Exception as e:
        print("Failed to send email: {}".format(e))