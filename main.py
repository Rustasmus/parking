
from registration import registration, authorization
from services import start_shift, create_talon, check_out, update_counter
from database import read_counter, create_counter, create_staffs
import os


def main():

    # staff_counter = 0
    # shift_counter = 0
    # talon_counter = 0
    if not os.path.exists(r'C:\Users\Rustas\PycharmProjects\parking_art\counter.txt'):
        create_counter(f'{0},{0},{0}')
    data_c = read_counter()
    # парсим полученные данные
    data_c = [int() for i in data_c.split(',')]
    staff_counter, shift_counter, talon_counter = data_c

    if not os.path.exists(r'C:\Users\Rustas\PycharmProjects\parking_art\staffs.txt'):
        a = {0: {'username': 0, 'password': 0, 'phone number': 0}}
        create_staffs(f'{a}')

    if not os.path.exists(r'C:\Users\Rustas\PycharmProjects\parking_art\talons.txt'):
        a = {0: {'car number': 0, 'check in': 0, 'check out': 0, 'total price': 0, 'status': 0}}
        create_staffs(f'{a}')
    if not os.path.exists(r'C:\Users\Rustas\PycharmProjects\parking_art\shifts.txt'):
        a = {0: {'date': 0, 'staff_id': 0, 'talons': 0}}
        create_staffs(f'{a}')
    # data_st = read_staffs()
    # парсим полученные данные
    # data_st = eval(data_st)
    # staff_counter = data_st.keys[-1]
    # username, password, phone_number = data_st[staff_counter]['username'], data_st[staff_counter]['password'], data_st[staff_counter]['phone_number']

    while True:
        action = input("Enter 1 to registration\n"
                       "Enter 2 to authorization\n").strip()
        if action == '1':
            is_reg = registration(staff_counter)
            if is_reg:
                staff_counter += 1
                update_counter(data=data_c, staff_counter=staff_counter)
                print("You registered success!")
            else:
                print("Registration failed!")
        elif action == '2':
            # authorization() return (True or False, staff_id)
            is_auth, staff_id = authorization()
            if is_auth:
                print("You authorized success!")
                while True:
                    action = input("Enter 1 to start shift\n"
                                   "Enter 2 to end shift\n"
                                   "Enter 3 to create tariff").strip()
                    if action == '1':
                        shift_counter += 1
                        staff_counter += 1
                        update_counter(data=data_c, staff_counter=staff_counter)
                        is_start = start_shift(shift_id=shift_counter, staff_id=staff_id)
                        if is_start:
                            print("Shift start!")
                        while True:
                            action = input(
                                "Enter 1 to check in auto\n"
                                "Enter 2 to check out auto\n"
                                "Enter 3 to go to menu").strip()

                            if action == '1':
                                talon_counter += 1
                                is_create_talon = create_talon(talon_id=talon_counter)
                                if is_create_talon:
                                    print("Talon created!")
                            elif action == '2':
                                car_number = input('Enter your car number for check out: ')
                                check_out(car_number=car_number)
                            elif action == '3':
                                pass
                            else:
                                print("Incorrect command!")
            else:
                print("Authorization failed!")
        else:
            print("Incorrect command!")


if __name__ == '__main__':
    main()

