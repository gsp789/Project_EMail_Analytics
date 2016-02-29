from Email import Email
from View import *
from import_email import *


def import_file(path):
    file = open(path)
    lines = file.readlines()
    to_addresses = get_to(lines)
    from_address = get_from(lines)
    cc = get_cc(lines)
    bcc = get_bcc(lines)
    time_sent = get_date(lines)
    subject = get_subject(lines)
    content = get_content(lines)
    return Email(time_sent, subject, content, from_address, to_addresses, cc, bcc)

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x50+500+300")
    app = Example(root)
    root.mainloop()

