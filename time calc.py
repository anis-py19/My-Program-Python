def calc(distance , speed):
    while distance <= 0 or distance >1500:
        distance = float(input("Re-Enter Distance Please: "))
    while speed <= 0 or speed > 300:
        speed = float(input("Re-Enter Speed Please: "))
    time = distance / speed 
    avg = round(time,2)
    avg = str(avg)
    avg = avg.split(".")
    hours = int(avg[0])
    minute = int(avg[1][:])
    return f"Time To Take {distance}km Is:{hours}h and {minute}min"
distance= float(input("Enter Your Distance in Km : "))
speed = float(input("Enter Your Speed In km/h: "))
print(calc(distance,speed))