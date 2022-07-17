PARKING_AMOUNT = 20
staffs = {}
talons = {}
shifts = {}
free_place = PARKING_AMOUNT


def create_counter(data):
    with open('counter.txt', mode='w') as file:
        file.write(data)


def read_counter():
    with open('counter.txt', mode='r') as file:
        data = file.read()
        return data


def create_staffs(data):
    with open('staffs.txt', mode='w') as file:
        file.write(f'{data}')


def read_staffs():
    with open('staffs.txt', mode='r') as file:
        data = file.read()
        return data
