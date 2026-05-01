import smtplib
import os
from email.mime.text import MIMEText
from decouple import config

def send_email(to, type, reservation_id, table_id, date, heure):
    
    # 1. Prépare le sujet et le contenu selon le type
    if type == "CONFIRMATION":
        subject = "✅ Confirmation de votre réservation"
        body = f"""
Bonjour,

Votre réservation est confirmée !

- Numéro de réservation : #{reservation_id}
- Table : {table_id}
- Date : {date}
- Heure : {heure}

Merci et à bientôt !
        """
    else:
        subject = "❌ Annulation de votre réservation"
        body = f"""
Bonjour,

Votre réservation a été annulée.

- Numéro de réservation : #{reservation_id}
- Table : {table_id}
- Date : {date}
- Heure : {heure}

Contactez-nous pour plus d'informations.
        """

    # 2. Crée le message email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From']    = config('EMAIL_FROM')
    msg['To']      = to

    # 3. Envoie via SMTP
    with smtplib.SMTP(config('SMTP_HOST', default='smtp.gmail.com'), 
                      int(config('SMTP_PORT', default=587))) as server:
        server.starttls()
        server.login(config('EMAIL_USER'), config('EMAIL_PASSWORD'))
        server.send_message(msg)
        print(f"[✓] Email envoyé à {to}")