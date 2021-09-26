# -*- coding: utf-8 -*-
# Python imports
from __future__ import unicode_literals
from contextlib import suppress
from typing import List, Optional

# lib imports
import boto3
from django.conf import settings
from email.mime.text import MIMEText
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# project imports
from utils import messages


ses_client = boto3.client(service_name='ses', region_name=settings.AWS_REGION)


def send_mail(
    to: List[str],
    subject: str,
    body: str,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    from_email: Optional[str] = settings.SERVER_EMAIL,
    reply_to: Optional[List[str]] = None,
):
    """
        Set Context

        Args:
            to (str, list): send mail to given email or emails
            body (str): content of body (html supported)
            subject (str): subject of the mail
            from_email (str): email of the sender if not given read from env
            bcc (str, list): add given emails to bcc
            cc (str, list): add given emails to cc
            reply_to (str, list): add given emails for reply

        Return:
            None

        Raises:
            Exception: if to address not provided
            Exception: if sending email fails
    """
    if cc is None:
        cc = []
    if bcc is None:
        bcc = []
    if reply_to is None:
        reply_to = []
    if not to:
        raise Exception(messages.EMAIL_TO_REQUIRED)
    message = {
        'Subject': {
            'Data': subject, 
            'Charset': 'UTF-8'
        },
        'Body': {
            'Html': {
                'Data': body, 
                'Charset': 'UTF-8'
            }
        },
    }
    destination = {
        'ToAddresses': to, 
        'CcAddresses': cc, 
        'BccAddresses': bcc
    }
    with suppress(ClientError):
        ses_client.send_email(
            Source=from_email,
            Destination=destination,
            Message=message,
            ReplyToAddresses=reply_to,
        )
    raise Exception(messages.EMAIL_SEND_FAIL)


def send_raw_mail(
    to: List[str],
    subject: str,
    body: str,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    from_email: Optional[str] = settings.SERVER_EMAIL,
    reply_to: Optional[List[str]] = None,
    attachment_file: Optional[str] = None,
):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to

    body = MIMEText(body)
    msg.attach(body)

    filename = attachment_file

    with open(filename, "rb") as attachment:
        part = MIMEApplication(
            attachment.read()
        )
        part.add_header(
            "Content-Disposition",
            "attachment",
            filename=filename
        )
    msg.attach(part)
    destination = {
        'ToAddresses': to,
        'CcAddresses': cc,
        'BccAddresses': bcc
    }
    response = ses_client.send_raw_email(
        Source=from_email,
        Destinations=destination,
        RawMessage={
            "Data": msg.as_string()
        },
        ReplyToAddresses=reply_to,
    )
    print(response)
