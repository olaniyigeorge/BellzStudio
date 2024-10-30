# newsletter/tasks.py

from celery import shared_task
from django.core.mail import send_mass_mail, send_mail
from BellzStudio.settings import DEFAULT_FROM_EMAIL
from main.models import User
from .models import Reader


@shared_task
def notify_subscribers_of_new_note(note_body_excerpt: str, level: int):
    """
    Sends email to all subscribers in that subscription level.
    """
    # Retrieve all newsletter signees
    subs = Reader.objects.filter(subscription_level__gte=level)
    print(f"---- Sending to {len(subs)} subs ----")
    # Prepare email data
    messages = []
    subject = "Exciting New Note For Your Subscription Level!"
    from_email = DEFAULT_FROM_EMAIL
    message = note_body_excerpt
    
    for sub in subs:
        recipient = sub.user.email
        messages.append((subject, message, from_email, [recipient]))
    
    # Send emails in bulk
    send_mass_mail(messages, fail_silently=False)
    
    return f"Sent {len(messages)} promotional emails."


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
