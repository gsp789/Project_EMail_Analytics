import os
from hashlib import md5

import import_email
from entities.Email import Email
from entities.EmailAddress import EmailAddress
from entities.Folder import Folder
from entities.Person import Person


def process_people(directory_path):
    for directory in os.listdir(directory_path):
        person = Person(directory)
        person.save()

        extract_folders(directory_path + directory + '/', person)


def extract_folders(directory_path, person):
    for directory in os.listdir(directory_path):
        folder = Folder(directory)
        folder.save()

        person.add_relationship("OWNS", folder)
        person.save()

        extract_emails(directory_path + directory + '/', folder)


def extract_emails(directory_path, folder_object):
    for file_name in os.listdir(directory_path):
        email_data = extract_data(directory_path + file_name)

        body_hash = md5(email_data['body'].encode('utf-8')).hexdigest()

        existing_emails = Email.get_entities(property_key="body_hash", property_value=body_hash)

        if len(existing_emails) > 0 and existing_emails[0].body == email_data['body']:
            existing_emails[0].add_relationship("IN", folder_object)
            email.save()
            continue

        email = Email(subject=email_data['subject'], date=email_data['date'], body=email_data['body'])
        email.save()

        email.add_relationship("IN", folder_object)

        sender_email = EmailAddress(email_data['from'])
        sender_email.save()
        email.add_relationship("SENDER", sender_email)

        for address_type in ["to", "cc", "bcc"]:
            for address in email_data[address_type]:
                email_address = EmailAddress(address)
                email_address.save()
                email.add_relationship(address_type.upper(), email_address)

        email.save()


def extract_data(file_name):
    file = open(file_name)
    email_text = file.readlines()

    subject = import_email.get_subject(email_text)
    date = import_email.get_date(email_text)
    body = import_email.get_content(email_text)

    sender_email = import_email.get_from(email_text)
    to_addresses = import_email.get_to(email_text)

    cc_addresses = import_email.get_cc(email_text)

    bcc_addresses = import_email.get_bcc(email_text)

    return {
        "subject": subject,
        "date": date,
        "body": body,
        "from": sender_email,
        "to": to_addresses,
        "cc": cc_addresses,
        "bcc": bcc_addresses
    }
