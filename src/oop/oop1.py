# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# BASE CLASS: VEHICLE

class Vehicle:
    pass

# VEHICLE CHILD 1: GROUND VEHICLES

class GroundVehicle(Vehicle):
    pass

# GROUND VEHICLE CHILDREN: CAR AND MOTORCYCLE

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# VEHICLE CHILD 2: FLIGHT VEHICLES

class FlightVehicle(Vehicle):
    pass

# FLIGHT VEHICLE CHILDREN: STARSHIP AND AIRPLANE

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass





