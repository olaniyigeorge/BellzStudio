# newsletter/tasks.py

from celery import shared_task
from django.core.mail import send_mass_mail
from django.conf import settings
from main.models import User


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_promotional_emails():
    """
    Sends promotional emails to all users in the NewsLetterSignee table.
    """
    # Retrieve all newsletter signees
    signees = User.objects.all()
    
    # Prepare email data
    messages = []
    subject = "Exciting Promotions Just for You!"
    from_email = settings.DEFAULT_FROM_EMAIL
    message = "Hello,\n\nDon't miss our exclusive promotions available this week!\n\nBest regards,\nYour Company"
    
    for signee in signees:
        recipient = signee.email
        messages.append((subject, message, from_email, [recipient]))
    
    # Send emails in bulk
    send_mass_mail(messages, fail_silently=False)
    
    return f"Sent {len(messages)} promotional emails."
