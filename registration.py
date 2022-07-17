from validate_data import validate_data, check_username
from database import read_staffs
from services import update_staffs


def registration(counter):
    name = input("Enter name: ").strip().capitalize()
    surname = input("Enter surname: ").strip().capitalize()
    phone_number = input("Enter your phone number").strip()
    password1 = input("Enter password: ").strip()
    password2 = input("Confirm password: ").strip()
    username = name + '.' + surname
    is_cd = validate_data(name=name, surname=surname, password1=password1, password2=password2,
                          phone_number=phone_number)
    is_unique = check_username(username=username)

    if is_cd is True and is_unique is True:
        data = read_staffs()
        staffs = eval(data)
        counter += 1
        staffs[counter] = {
            "username": username,
            "phone number": phone_number,
            "password": password2,
        }
        update_staffs(staffs)
        return True
    else:
        print('Человек с такими данными уже есть')
        return False


def authorization():
    username = input("Enter your username: ").strip()
    password = input("Enter password: ").strip()
    # staffs.items() == (keys, values == {'username', 'password'})
    data_st = read_staffs()
    # парсим полученные данные
    data_st = eval(data_st)
    for staff_id, staff in data_st.items():
        if staff['username'] == username and staff['password'] == password:
            return True, staff_id
    return False, 0
