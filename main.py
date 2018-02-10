import sys 

class Car:
    def __init__(self, *args, **kwargs):
        self._reg_no = args[0]
        self._color = args[1]

class ParkingLot:
    def __init__(self, slots_count=0):
        self._slots_count = slots_count
        self._slots = [0 for x in range(self._slots_count)]
        print "Created a parking lot with {} slots".format(self._slots_count)

    def park(self, *args, **kwargs):
        for index, slot in enumerate(self._slots):
            if slot == 0:
                car = Car(*args, **kwargs)
                self._slots[index] = car
                print "Allocated slot number: {}".format(index+1)
                return
        print "Sorry, parking lot is full"
        
    def leave(self, slot_number):
        slot_number = int(slot_number)
        if slot_number <= self._slots_count:
            self._slots[slot_number-1] = 0
            print "Slot number {} is free".format(slot_number)
        else:
            print "invalid slot number"

    def slot_number_for_registration_number(self, reg_no):
        for index, car in enumerate(self._slots):
            if car and car._reg_no == reg_no:
                print index + 1
                return
        print "Not found"

    def slot_numbers_for_cars_with_colour(self, color):
        slots = []
        for index, car in enumerate(self._slots):
            if car and car._color == color:
                slots.append(index+1)

        if slots:
            print ",".join([str(x) for x in slots])
        else:
            print "No car with such color is parked"
    
    def registration_numbers_for_cars_with_colour(self, color):
        reg_nos = []
        for index, car in enumerate(self._slots):
            if car and car._color == color:
                reg_nos.append(car._reg_no)
                
        if reg_nos:
            print ",".join(reg_nos)
        else:
            print "No car with such color is parked"

    def status(self):
        print "%-16s%-20s%-16s"%("Slot No.","Registration No","Colour") 
        for index, car in enumerate(self._slots):
            if car:
                print "%-16s%-20s%-16s"%(index, car._reg_no, car._color)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as f:
            while True:
                line = f.readline().rstrip()
                if not line: break
                line = line.split(" ")
                if line[0] == "create_parking_lot":
                    parking_lot = ParkingLot(int(line[1]))
                else:
                    getattr(parking_lot, line[0])(*line[1:])
    else:
        user_input = raw_input().split(" ")
        parking_lot = ParkingLot(int(user_input[1]))
        user_input = raw_input()
        while user_input != "exit" and user_input != "\n":
            user_input = user_input.split(" ")
            getattr(parking_lot, user_input[0])(*user_input[1:])
            user_input = raw_input()

