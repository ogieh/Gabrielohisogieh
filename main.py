statement = 'Hello World'
print(statement)

def Newtons_second_law():
    Mass = float(input("Enter the mass of the object: "))
    Acceleration = float(input("Enter the acceleration of the object: "))
    Force = Mass * Acceleration
    print("The force is: " , Force)

def average_speed():
    Distance = float(input("Enter the distance traveled (in meters): "))
    Time = float(input("Enter the time taken (in seconds): "))
    Speed = Distance / Time
    print("The average speed is: " , Speed , "m/s")

def ohms_law():
    Voltage = float(input("Enter the voltage (in volts): "))
    Resistance = float(input("Enter the resistance (in ohms): "))
    Current = Voltage / Resistance
    print("The current is: " , Current , "amperes")
def impulse_momentum():
    Mass = float(input("Enter the mass of the object (in kg): "))
    final_velocity = float(input("Enter the final velocity (in m/s): "))
    initial_velocity = float(input("Enter the initial velocity (in m/s): "))
    impulse_momentum = Mass * (final_velocity - initial_velocity)
    print("The impulse momentum is: " , impulse_momentum , "kg·m/s")

ohms_law()
impulse_momentum()
average_speed()
Newtons_second_law()