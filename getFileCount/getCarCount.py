
import re

car_list = []
for line in open('resource/car.txt'):
    searchObj = re.search('CAR-[0-9]{4}-[0-9]{2}-[0-9]{3}', line)
    car = "" if searchObj is None else searchObj.group()

    if car != "":
        car_list.append(car)

print(len(car_list))