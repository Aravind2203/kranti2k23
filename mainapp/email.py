from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
def sendmail(name,email):
    content=f"""<h2>Dear {name},</h2><br>,
    Thank you for registering for our national level technical symposium, <strong>Kranti2k23</strong>. We are excited to have you join us for this exciting event that will showcase some of the latest technological advancements in the industry.

    Your registration has been confirmed and we look forward to seeing you at the event. Here are some important details that you will need to keep in mind:
<br>
    Date: 24-03-2023<br>
    Time: 8:00 AM<br>
    Venue: Meenakshi Sundararajan Engineering College, Kodambakkam
    <br>
    Please make sure to arrive at the venue on time and carry a valid ID proof with you. This will be required for verification purposes.
<br>
    If you have any questions or concerns, please do not hesitate to reach out to us. We will be more than happy to assist you.
<br>
    Thank you once again for registering for Kranti2023. We look forward to your participation and hope that you have a great experience at the event.
<br>
    Best regards,<br>
    Team kranti
    """
    message = Mail(
    from_email='kranti2k23@gmail.com',
    to_emails=email,
    subject='Thankyou for registration',
    html_content=content)
    try:
        sg = SendGridAPIClient(settings.SKEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)