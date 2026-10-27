from datetime import datetime


# ==========================================
# 1. VEHICLE CLASS
# ==========================================

class Vehicle:
    def __init__(self, vehicle_id, vehicle_number, owner_name,
                 vehicle_type, parking_slot, entry_time=None):

        self.vehicle_id = vehicle_id
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.parking_slot = parking_slot
        self.entry_time = entry_time or datetime.now()
        self.exit_time = None
        self.status = "Parked"
        self.parking_fee = 0

    def display(self):
        print("-" * 45)
        print(f"Vehicle ID     : {self.vehicle_id}")
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Owner Name     : {self.owner_name}")
        print(f"Vehicle Type   : {self.vehicle_type}")
        print(f"Parking Slot   : {self.parking_slot}")
        print(f"Entry Time     : {self.entry_time}")
        print(f"Exit Time      : {self.exit_time}")
        print(f"Status         : {self.status}")
        print(f"Parking Fee    : Rs. {self.parking_fee}")
        print("-" * 45)


# ==========================================
# 2. VEHICLE LINKED LIST
# ==========================================

class VehicleNode:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.next = None


class VehicleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, vehicle):
        new_node = VehicleNode(vehicle)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def search(self, vehicle_number):
        current = self.head

        while current:
            if current.vehicle.vehicle_number.lower() == vehicle_number.lower():
                return current.vehicle
            current = current.next

        return None

    def delete(self, vehicle_number):
        current = self.head
        previous = None

        while current:
            if current.vehicle.vehicle_number.lower() == vehicle_number.lower():

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return current.vehicle

            previous = current
            current = current.next

        return None

    def display_all(self):
        current = self.head

        if current is None:
            print("No vehicle records found.")
            return

        while current:
            current.vehicle.display()
            current = current.next

    def get_all(self):
        vehicles = []
        current = self.head

        while current:
            vehicles.append(current.vehicle)
            current = current.next

        return vehicles


# ==========================================
# 3. PARKING MANAGEMENT SYSTEM
# ==========================================

class ParkingManagementSystem:

    def __init__(self, total_slots=10):
        self.total_slots = total_slots
        self.vehicle_list = VehicleLinkedList()
        self.next_vehicle_id = 1
        self.parking_slots = {
            slot: None for slot in range(1, total_slots + 1)
        }

        self.parking_rates = {
            "Car": 50,
            "Bike": 20,
            "Scooter": 15,
            "Truck": 100
        }

    # --------------------------------------
    # Generate Vehicle ID
    # --------------------------------------

    def generate_vehicle_id(self):
        vehicle_id = self.next_vehicle_id
        self.next_vehicle_id += 1
        return vehicle_id

    # --------------------------------------
    # Find Available Slot
    # --------------------------------------

    def find_available_slot(self):
        for slot, vehicle in self.parking_slots.items():
            if vehicle is None:
                return slot

        return None

    # --------------------------------------
    # Add Vehicle
    # --------------------------------------

    def add_vehicle(self):
        print("\n========== VEHICLE ENTRY ==========")

        vehicle_number = input("Enter vehicle number: ").strip().upper()

        if not vehicle_number:
            print("Vehicle number cannot be empty.")
            return

        if self.vehicle_list.search(vehicle_number):
            print("A vehicle with this number already exists.")
            return

        owner_name = input("Enter owner name: ").strip()

        if not owner_name:
            print("Owner name cannot be empty.")
            return

        print("\nVehicle Types:")
        print("1. Car")
        print("2. Bike")
        print("3. Scooter")
        print("4. Truck")

        choice = input("Select vehicle type: ").strip()

        vehicle_types = {
            "1": "Car",
            "2": "Bike",
            "3": "Scooter",
            "4": "Truck"
        }

        if choice not in vehicle_types:
            print("Invalid vehicle type.")
            return

        vehicle_type = vehicle_types[choice]
        slot = self.find_available_slot()

        if slot is None:
            print("Parking is full. No available slots.")
            return

        vehicle = Vehicle(
            self.generate_vehicle_id(),
            vehicle_number,
            owner_name,
            vehicle_type,
            slot
        )

        self.vehicle_list.insert(vehicle)
        self.parking_slots[slot] = vehicle

        print("\nVehicle parked successfully!")
        print(f"Vehicle ID : {vehicle.vehicle_id}")
        print(f"Parking Slot: {slot}")
        print(f"Entry Time : {vehicle.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # --------------------------------------
    # Search Vehicle
    # --------------------------------------

    def search_vehicle(self):
        print("\n========== SEARCH VEHICLE ==========")

        vehicle_number = input(
            "Enter vehicle number: "
        ).strip().upper()

        vehicle = self.vehicle_list.search(vehicle_number)

        if vehicle:
            vehicle.display()
        else:
            print("Vehicle not found.")

    # --------------------------------------
    # Display All Vehicles
    # --------------------------------------

    def display_vehicles(self):
        print("\n========== ALL VEHICLE RECORDS ==========")
        self.vehicle_list.display_all()

    # --------------------------------------
    # Display Parking Slots
    # --------------------------------------

    def display_parking_slots(self):
        print("\n========== PARKING SLOT STATUS ==========")

        for slot, vehicle in self.parking_slots.items():
            if vehicle is None:
                print(f"Slot {slot}: Available")
            else:
                print(
                    f"Slot {slot}: Occupied by "
                    f"{vehicle.vehicle_number} ({vehicle.vehicle_type})"
                )

        occupied = sum(
            1 for vehicle in self.parking_slots.values()
            if vehicle is not None
        )

        print(f"\nTotal Slots     : {self.total_slots}")
        print(f"Occupied Slots  : {occupied}")
        print(f"Available Slots : {self.total_slots - occupied}")

    # --------------------------------------
    # Calculate Parking Fee
    # --------------------------------------

    def calculate_fee(self, vehicle, exit_time):
        duration = exit_time - vehicle.entry_time

        # Charge for every started hour, minimum one hour
        hours = max(1, (int(duration.total_seconds()) + 3599) // 3600)

        rate = self.parking_rates.get(vehicle.vehicle_type, 20)

        return hours * rate

    # --------------------------------------
    # Vehicle Exit
    # --------------------------------------

    def vehicle_exit(self):
        print("\n========== VEHICLE EXIT ==========")

        vehicle_number = input(
            "Enter vehicle number: "
        ).strip().upper()

        vehicle = self.vehicle_list.search(vehicle_number)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status != "Parked":
            print("This vehicle has already exited.")
            return

        vehicle.exit_time = datetime.now()
        vehicle.parking_fee = self.calculate_fee(
            vehicle, vehicle.exit_time
        )
        vehicle.status = "Exited"

        self.parking_slots[vehicle.parking_slot] = None

        print("\nVehicle exited successfully!")
        print(f"Vehicle Number: {vehicle.vehicle_number}")
        print(f"Entry Time    : {vehicle.entry_time}")
        print(f"Exit Time     : {vehicle.exit_time}")
        print(f"Parking Fee   : Rs. {vehicle.parking_fee}")

    # --------------------------------------
    # Update Vehicle Information
    # --------------------------------------

    def update_vehicle(self):
        print("\n========== UPDATE VEHICLE ==========")

        vehicle_number = input(
            "Enter vehicle number: "
        ).strip().upper()

        vehicle = self.vehicle_list.search(vehicle_number)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status != "Parked":
            print("Only currently parked vehicles can be updated.")
            return

        print("1. Update Owner Name")
        print("2. Update Vehicle Type")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_name = input("Enter new owner name: ").strip()

            if new_name:
                vehicle.owner_name = new_name
                print("Owner name updated successfully.")
            else:
                print("Owner name cannot be empty.")

        elif choice == "2":
            print("1. Car")
            print("2. Bike")
            print("3. Scooter")
            print("4. Truck")

            type_choice = input("Select new vehicle type: ").strip()

            vehicle_types = {
                "1": "Car",
                "2": "Bike",
                "3": "Scooter",
                "4": "Truck"
            }

            if type_choice in vehicle_types:
                vehicle.vehicle_type = vehicle_types[type_choice]
                print("Vehicle type updated successfully.")
            else:
                print("Invalid vehicle type.")

        else:
            print("Invalid choice.")

    # --------------------------------------
    # Delete Vehicle Record
    # --------------------------------------

    def delete_vehicle(self):
        print("\n========== DELETE VEHICLE RECORD ==========")

        vehicle_number = input(
            "Enter vehicle number: "
        ).strip().upper()

        vehicle = self.vehicle_list.search(vehicle_number)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.status == "Parked":
            self.parking_slots[vehicle.parking_slot] = None

        deleted_vehicle = self.vehicle_list.delete(vehicle_number)

        if deleted_vehicle:
            print("Vehicle record deleted successfully.")

    # --------------------------------------
    # Parking Statistics
    # --------------------------------------

    def parking_statistics(self):
        print("\n========== PARKING STATISTICS ==========")

        vehicles = self.vehicle_list.get_all()

        total_records = len(vehicles)
        parked = sum(1 for v in vehicles if v.status == "Parked")
        exited = sum(1 for v in vehicles if v.status == "Exited")

        total_revenue = sum(
            v.parking_fee for v in vehicles
        )

        available = self.total_slots - parked

        print(f"Total Vehicle Records : {total_records}")
        print(f"Currently Parked      : {parked}")
        print(f"Vehicles Exited       : {exited}")
        print(f"Available Slots       : {available}")
        print(f"Total Revenue         : Rs. {total_revenue}")

    # --------------------------------------
    # Main Menu
    # --------------------------------------

    def main_menu(self):
        while True:
            print("\n" + "=" * 40)
            print("      PARKING MANAGEMENT SYSTEM")
            print("=" * 40)

            print("1. Add Vehicle")
            print("2. Search Vehicle")
            print("3. Display All Vehicles")
            print("4. Display Parking Slots")
            print("5. Vehicle Exit")
            print("6. Update Vehicle")
            print("7. Delete Vehicle Record")
            print("8. Parking Statistics")
            print("9. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_vehicle()

            elif choice == "2":
                self.search_vehicle()

            elif choice == "3":
                self.display_vehicles()

            elif choice == "4":
                self.display_parking_slots()

            elif choice == "5":
                self.vehicle_exit()

            elif choice == "6":
                self.update_vehicle()

            elif choice == "7":
                self.delete_vehicle()

            elif choice == "8":
                self.parking_statistics()

            elif choice == "9":
                print("Thank you for using the Parking Management System!")
                break

            else:
                print("Invalid choice. Please try again.")


# ==========================================
# 4. PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    parking_system = ParkingManagementSystem(total_slots=10)
    parking_system.main_menu()
