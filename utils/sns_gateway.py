# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress
from typing import Optional

# lib imports
import boto3
from django.conf import settings

sns_client = boto3.client(
    service_name="sns", region_name=settings.AWS_REGION, endpoint_url=settings.AWS_SNS_ENDPOINT
)


def send_sms(
    phone_number: str, subject: str, message: str, transaction: Optional[bool] = True
) -> str:
    """
    Send Sms to the given number

    Args:
        phone_number (str): phone number with country code
        subject (str): subject more like topic
        message (str): message content
        transaction (bool): this set if the message is transactional of not

    Return:
        message_id
    """
    message_id = ""
    with suppress(Exception):
        publish_result = sns_client.publish(
            PhoneNumber=phone_number,
            Message=message,
            Subject=subject,
            MessageAttributes={
                "AWS.SNS.SMS.SMSType": {
                    "DataType": "String",
                    "StringValue": "Transactional" if transaction else "Promotional",
                }
            },
        )
        message_id = publish_result["MessageId"]
    return message_id
