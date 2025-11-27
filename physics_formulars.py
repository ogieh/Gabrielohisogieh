def newtons_second_law():
    Mass = float(input("Enter the mass of the object (in Kilogram): "))
    Acceleration = float(input("Enter the accelaration of the object (in meters per second square): "))
    Force = Mass * Acceleration
    print("The force at which the object is moving is: ", Force)

def ohms_law():
    Current = float(input("Enter the current flowing through the circuit: "))
    Resistance = float(input("Enter the resistance of the circuit: "))
    Voltage = Current * Resistance
    print("The voltage flowing through the circuit is" , Voltage)




def main():
    print("1. Newton's second law")
    print("2. ohm's law")
    print("3. kinectic energy")
    print("4. Velocity")
    print("5. Impulsive momentum")