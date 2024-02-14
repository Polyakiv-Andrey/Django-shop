from sendgrid.helpers.mail import (Mail, Email, Personalization)
from django.conf import settings

import sendgrid
from django_shop import settings
from django_shop.celery import app

from site_detail.models import SiteDetail


@app.task
def send_email_task(template, data, to):
    site, created = SiteDetail.objects.get_or_create(id=1)
    if site.email:
        email = site.email
    else:
        email = settings.DEFAULT_FROM_EMAIL
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    mail = Mail()
    mail.template_id = template
    mail.from_email = Email(email)
    personalization = Personalization()
    personalization.add_to(Email(to))
    personalization.dynamic_template_data = data
    mail.add_personalization(personalization)
    sg.client.mail.send.post(request_body=mail.get())