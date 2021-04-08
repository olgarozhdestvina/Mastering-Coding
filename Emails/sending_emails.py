import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # similar to os.path


def email_sending():
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Dummy'
    email['to'] = 'youremailhere@gmail.com'
    email['subject'] = 'You inherited 1,000,000,000 dollars!'

    email.set_content(html.substitute({'name':'TinTin', 'lastName':'Smirnov'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls() # connect to the server
        smtp.login('ddduuummmyyy46@gmail.com', 'yesYes123!')
        smtp.send_message(email)
        return 'all good'

email_sending()
