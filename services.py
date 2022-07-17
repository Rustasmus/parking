from database import shifts, talons, create_counter, create_staffs
import datetime


def start_shift(shift_id, staff_id):
    date = datetime.datetime.now()
    shifts[shift_id] = {
        'date': date,
        'staff_id': staff_id,
        'talons': []
    }
    return True


def create_talon(talon_id, free_place):
    car_number = input("Enter car number: ").strip()
    check_in = datetime.datetime.now().strptime(%Y.%m.%d_%H:%M)
    check_out = 0
    total_price = 0
    status = 'parking'
    talons[talon_id] = {
        'car number': car_number,
        'check in': check_in,
        'check out': check_out,
        'total price': total_price,
        'status': status
    }
    return True


def check_out(car_number):
    for talon_id, talon in talons.items():
        if talon['car_number'] == car_number :
            status = input('Enter 1 if free\n'
                           'Enter 2 if not free\n')
            if status == '1':
                my_talon = talons[talon_id]
                my_talon['check out'] = datetime.datetime.now()
                my_talon['status'] = 'free'
                print(f'''
                                Your talon: {talon_id}

                                Your car number: {my_talon['car number']}
                                Check in: {my_talon['check_in']}
                                Check out: {my_talon['check out']}
                                Duration: {my_talon['status']}
                                Tariff: {my_talon['status']}
                                Total price: {my_talon['status']}
                                Goodbay
                                ''')
            elif status == '2':
                my_talon = talons[talon_id]
                date_end = datetime.datetime.now()
                duration = date_end - my_talon['check in']
                duration = duration.seconds / 60
                total_price = 0
                my_talon['check out'] = datetime.datetime.now()
                my_talon['status'] = 'free'
                my_talon['total price'] = total_price
                print(f'''
                Your talon: {talon_id}
                
                Your car number: {my_talon['car number']}
                Check in: {my_talon['check_in']}
                Check out: {my_talon['check out']}
                Duration: {duration} min
                Tariff: ...
                Total price: {total_price}
                Goodbay
                ''')
    return False


def update_counter(data, staff_counter):
    data.pop(0)
    data.insert(0, staff_counter)
    new_data = list(map(str, data))

    new_data = ','.join(new_data)
    create_counter(new_data)


def update_staffs(staffs):
    new_data = staffs
    create_staffs(new_data)
