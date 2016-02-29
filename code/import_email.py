def get_date(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith("Date:"):
            return line[5:].strip(' \n')
    return None


def get_from(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith("From:"):
            return line[5:].strip(' \n')
    return None


# TODO: Refactor to only include email address (according to RFC spec: https://en.wikipedia.org/wiki/Email_address#Syntax)
#TODO: Refactor to not return duplicates
def get_to(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith("To:"):
            to_string = line[3:].strip(' \n')
            i += 1
            line = lines[i]
            while line.count(':') == 0:
                to_string += line.strip('\t \n')
                i += 1
                line = lines[i]
            i -= 1
            line = lines[i]
            return to_string.replace(', ', ',').split(',')
    return []


def get_subject(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('Subject:'):
            return line[8:].strip(' \n')
    return ""


def get_cc(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('Cc:'):
            cc_string = line[3:].strip(' \n')
            i += 1
            line = lines[i]
            while line.count(':') == 0:
                cc_string += line.strip('\t \n')
                i += 1
                line = lines[i]
            i -= 1
            line = lines[i]
            if cc_string:
                return cc_string.replace(', ', ',').split(',')
    return []


def get_bcc(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('Bcc:'):
            bcc_string = line[4:].strip(' \n')
            i += 1
            line = lines[i]
            while line.count(':') == 0:
                bcc_string += line.strip('\t \n')
                i += 1
                line = lines[i]
            i -= 1
            line = lines[i]
            if bcc_string:
                return bcc_string.replace(', ', ',').split(',')
    return []


def get_content(lines):
    content = ''
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('X-FileName:'):
            i += 1
            while i < len(lines):
                line = lines[i]
                content += line + '\n'
                i += 1
            return content
    return None
