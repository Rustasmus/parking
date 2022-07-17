from database import read_staffs


def validate_data(name, surname, phone_number, password1, password2):
    if password1 == password2 and len(name) > 1 and len(surname) > 1 and phone_number.startswith('0') \
            and phone_number.isdigit():
        return True
    else:
        return False


def check_username(username):
    data = read_staffs()
    staffs = eval(data)
    for staff in staffs.values():
        if username != staff["username"]:
            continue
        else:
            return False
    return True
