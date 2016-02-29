import unittest
import import_email
import settings
from entities.Folder import Folder
from extract_emails import extract_data, extract_emails, process_people
from tests import test_inputs


class EmailImportTests(unittest.TestCase):
    def test_get_date(self):
        self.assertEqual(import_email.get_date(test_inputs.get_valid_email_text()), "Fri, 1 Dec 2000 01:12:00 -0800 (PST)")

    def test_get_date_None(self):
        self.assertEqual(import_email.get_date(test_inputs.get_non_email_text()), None)

    def test_get_from(self):
        self.assertEqual(import_email.get_from(test_inputs.get_valid_email_text()), 'kayne.coulter@enron.com')

    def test_get_from_None(self):
        self.assertEqual(import_email.get_from(test_inputs.get_non_email_text()), None)

    def test_get_to(self):
        answer = ['larry.jester@enron.com', 'jay.wills@enron.com', 'cyril.price@enron.com', 'john.kinser@enron.com',
                  'rudy.acevedo@enron.com', 'richard.hrabal@enron.com', 'wayne.herndon@enron.com',
                  'lawrence.clayton@enron.com']
        self.assertEqual(import_email.get_to(test_inputs.get_valid_email_text()), answer)

    def test_get_to_None(self):
        self.assertEqual(import_email.get_to(test_inputs.get_non_email_text()), [])

    def test_get_subject(self):
        self.assertEqual(import_email.get_subject(test_inputs.get_valid_email_text()), 'Transmission Rate Part II')

    def test_get_subject_None(self):
        self.assertEqual(import_email.get_subject(test_inputs.get_non_email_text()), "")

    def test_get_cc(self):
        answer = ['Random CC', 'Other Random CC']
        self.assertEqual(import_email.get_cc(test_inputs.get_valid_email_text()), answer)

    def test_get_cc_None(self):
        self.assertEqual(import_email.get_cc(test_inputs.get_non_email_text()), [])

    def test_get_bcc(self):
        answer = ['Random BCC', 'Other Random BCC']
        self.assertEqual(import_email.get_bcc(test_inputs.get_valid_email_text()), answer)

    def test_get_bcc_None(self):
        self.assertEqual(import_email.get_bcc(test_inputs.get_non_email_text()), [])

    def test_get_Content(self):
        answer = ''
        answer += 'Sorry about that, here it is for real this time.\n'
        answer += 'Second Content Line\n'
        self.assertEqual(import_email.get_content(test_inputs.get_valid_email_text()), answer)

    def test_get_content_None(self):
        self.assertEqual(import_email.get_content(test_inputs.get_non_email_text()), None)


# class ExtractDataTest(unittest.TestCase):
#     def setUp(self):
#         settings.GRAPH.delete_all()
#
#     def tearDown(self):
#         pass
#         # settings.GRAPH.delete_all()
#
#     def test_this_works(self):
#         email = process_people('test_data/')

if __name__ == '__main__':
    unittest.main()
