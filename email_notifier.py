import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import cv2
import threading
from datetime import datetime

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

# To send emails 
def _send_email_task(person_name, receiver_email, frame, location):
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print(
            "[WARNING] Email credentials not set. Skipping email notification. "
            "Set SENDER_EMAIL and SENDER_PASSWORD as environment variables to enable email alerts."
        )
        return
    try:
        print(f"[INFO] Background task started: Sending email to {receiver_email}...")
        
        # 1. Current Date and Time
        now = datetime.now()
        # Format example: 09-Jul-2026 at 02:14 PM
        dt_string = now.strftime("%d-%b-%Y at %I:%M:%S %p") 
        
        msg = MIMEMultipart()
        msg['Subject'] = f"🚨 URGENT: {person_name} has been Spotted!"
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email

        # 2. Email format
        body = f"""Hello,

Our AI system has successfully detected {person_name} on our camera feed.

📍 DETECTION DETAILS:
-------------------------------------------------
• Person Name     : {person_name}
• Date & Time     : {dt_string}
• Camera Location : {location}
-------------------------------------------------

Please find the attached live screenshot for reference.

Regards,
AI Face Recognition System"""
        
        msg.attach(MIMEText(body, 'plain'))

        # Image attach
        ret, buffer = cv2.imencode('.jpg', frame)
        if ret:
            image_attachment = MIMEImage(buffer.tobytes(), name=f"{person_name}_spotted.jpg")
            msg.attach(image_attachment)
        else:
            print("[WARNING] Image encode failed, sending without image.")

        # Email sending logic
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"Email successfully delivered to {receiver_email} for {person_name}")
    except Exception as e:
        print(f"Failed to send email from main app: {e}")


def trigger_email_alert(person_name, receiver_email, frame, location):
    email_thread = threading.Thread(
        target=_send_email_task, 
        args=(person_name, receiver_email, frame, location), 
        daemon=True 
    )
    email_thread.start()