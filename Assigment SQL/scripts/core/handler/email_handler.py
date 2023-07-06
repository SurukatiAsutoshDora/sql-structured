import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.schemas.inventory_schemas import Email
from tabulate import tabulate
import pandas as pd
from scripts.logging.logs import logger
from scripts.constants.email_constants import email_object
from scripts.db.mongo import Item_handler
from json2html import *


class Email_handler:
    """this class helps in building an smtp mail structure for sending to the recepient"""

    def send_email(self, Email: Email):
        sender_email = email_object.email_name
        sender_password = email_object.email_password
        receiver_email = Email.rec_email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Total Price Of The Inventory List"

        inventory_object = Item_handler()
        result = inventory_object.find_total()
        get_list = inventory_object.fetch()
        html_table = json2html.convert(json=get_list)

        css_styles = f'''
        <html>
        <head>
        <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th, td {{
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}

        th {{
            background-color: #f2f2f2;
        }}
        </style>
        </head>
        <body>
        {html_table}
        </body>
        </html>
        '''

        html_table_with_styles = f'{css_styles}'
        body = str(result)
        message.attach(MIMEText(("THESE ARE THE ITEMS IN YOUR INVENTORY :\n" +
                       html_table_with_styles + "\n Total amount : " + body), "html"))
        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            logger.info({"message": "Email sent successfully"})
            return {"message": "Email sent successfully"}

        except Exception as e:
            logger.error({"message": str(e)})
            return {"message": str(e)}
