def physics_and_maths_operations_option():
    print("\nphysics and maths operations option:")
    print("a. area of rectangle ")
    print("b. heat capacity ")
    print("c. volume of cone ")
    print("d. kinetic energy ")
    print("e. potential energy ")


physics_and_maths_operations_option()
options =input("pick an option from a to e")
if options == 'a':

    breath = int(input("enter breath of rectangle  "))
    length = int(input("enter height of rectangle  "))
    area_of_rectangle = breath * length
    print(area_of_rectangle)
    
elif options == 'b':
    mass = int(input("Enter mass of object  "))
    specific_heat_capacity = int(input("enter specific heat capacity of object "))
    change_in_temperature = int(input("enter change in temperature of object "))
    heat_capacity = mass * specific_heat_capacity * change_in_temperature
    print(heat_capacity)

elif options == 'c':
    radius = int(input("enter radius of the cone  "))
    height = int(input("enter height of the cone  "))
    volume_of_cone = 1/3 * 3.142 * radius**2 * height
    print(volume_of_cone)

elif options == 'd':
    mass = int(input("enter mass number  "))
    velocity = int(input("enter velocity of the object  "))
    kinetic_energy= 0.5 * mass * velocity**2
    print(kinetic_energy)

elif options == 'e':
    mass = int(input("enter the mass of the PE  "))
    gravity = int(input("enter the acceleration due gravity of the PE  "))
    height = int(input("enter the height of the PE  "))
    potential_energy = mass * gravity * height
    print(potential_energy)
else :
    print("invalid option selected")
