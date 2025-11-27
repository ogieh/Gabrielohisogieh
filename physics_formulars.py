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

def kinectic_energy():
    Mass = float(input("Enter the mass of the object (in Kilogram): "))
    Velocity = float(input("Enter the speed at which the object is moving (in meters per second): "))
    kinectic_energy = Mass * (Velocity * Velocity)
    print("The kinectic energy the body possesses is ", kinectic_energy)

def velocity():
    Distance = float(input("Enter the distance travelled by the body: "))
    Time = float(input("Enter the time taken to cover the distance: "))
    velocity = Distance / Time
    print("The velocity the object is moving at is ", velocity)





def main():
    print("1. Newton's second law")
    print("2. ohm's law")
    print("3. kinectic energy")
    print("4. Velocity")
    print("5. Impulsive momentum")