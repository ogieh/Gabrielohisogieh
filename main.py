#statement = 'Hello World'
#print(statement)

def Newtons_second_law():
    mass = float(input("Enter the mass of the object: "))
    acceleration = float(input("Enter the acceleration of the object: "))
    force = mass * acceleration
    print("The force is: " , force)

def average_speed():
    distance = float(input("Enter the distance traveled (in meters): "))
    time = float(input("Enter the time taken (in seconds): "))
    speed = distance / time
    print("The average speed is: " , speed , "m/s")

def ohms_law():
    voltage = float(input("Enter the voltage (in volts): "))
    resistance = float(input("Enter the resistance (in ohms): "))
    current = voltage / resistance
    print("The current is: " , current , "amperes")
def impulse_momentum():
    mass = float(input("Enter the mass of the object (in kg): "))
    final_velocity = float(input("Enter the final velocity (in m/s): "))
    initial_velocity = float(input("Enter the initial velocity (in m/s): "))
    impulse_momentum = mass * (final_velocity - initial_velocity)
    print("The impulse momentum is: " , impulse_momentum , "kg·m/s")
def kinectic_energy():
    num = 0.5
    mass = float(input("Enter the mass of the object: "))
    velocity = float(input("Enter the velocity the object is moving at: "))
    kinectic_energy = num * mass * (velocity * 2)

#-------------------------------
#           main function
#-------------------------------
def main():
    print("Choose a calculation to perform:")
    print("1. Newton's Second Law")
    print("2. Average Speed")
    print("3. Ohm's Law")
    print("4. Impulse Momentum")
    print("5. Kinetic Energy")

    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        Newtons_second_law()
    elif choice == '2':
        average_speed()
    elif choice == '3':
        ohms_law()
    elif choice == '4':
        impulse_momentum()
    elif choice == '5':
        kinectic_energy()
    else:
        print("Invalid choice. Please select a valid option.")

main()