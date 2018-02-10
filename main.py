import sys 
from ParkingLot import ParkingLot
from Car import Car

if __name__ == "__main__":
    if len(sys.argv) > 1: #case 1: input from file
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
    else: #case 2: interactive input
        user_input = raw_input().split(" ")
        parking_lot = ParkingLot(int(user_input[1]))
        user_input = raw_input()
        while user_input != "exit" and user_input != "\n":# repeat till input is not equal to exit or newline
            user_input = user_input.split(" ")
            getattr(parking_lot, user_input[0])(*user_input[1:])
            user_input = raw_input()

