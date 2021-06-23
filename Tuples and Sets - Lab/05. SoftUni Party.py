num = int(input())
def input_guests(number):
    guests = set()
    for _ in range(number):
        guests.add(input())
    return guests


def guests_come(guests):
    command = input()
    while command != "END":
        current_guest = command
        if current_guest in guests:
            guests.remove(current_guest)
        command = input()
    return guests


def print_data(guests):
    guests = sorted(guests)
    print(len(guests))
    for guest in guests:
        print(guest)


guests = input_guests(num)
guests_come(guests)
print_data(guests)
