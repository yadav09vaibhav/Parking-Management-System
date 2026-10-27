

# Parking Management System

A Python-based, menu-driven Parking Management System that demonstrates object-oriented programming (OOP) and data structures. It helps manage vehicle entry and exit, parking slots, vehicle records, parking fees, and parking statistics.

## Features

- Register and park a vehicle
- Automatically assign an available parking slot
- Search for a vehicle by its registration number
- Display all vehicle records
- View parking-slot availability
- Record vehicle exit and calculate parking fees
- Update vehicle owner or vehicle type
- Delete vehicle records
- Display parking statistics and recorded revenue
- Maintain vehicle records using a singly linked list
- Use a slot map to track occupied and available spaces

## Technologies Used

- **Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Data Structures:** Singly linked list and dictionary
- **Interface:** Command-line / console menu
- **Standard library:** `datetime`

## Project Structure

```text
Parking-Management-System/
├── parking_management.py
└── README.md
```

## Requirements

- Python 3.8 or later recommended
- No third-party packages are required

## How to Run

1. Install Python 3 if it is not already installed.
2. Save the program code in a file named `parking_management.py`.
3. Open a terminal or command prompt in the project folder.
4. Run:

   ```bash
   python parking_management.py
   ```

   On some systems, use:

   ```bash
   python3 parking_management.py
   ```

5. Choose an option from the menu and follow the prompts.

## Menu Options

| Option | Operation |
|---|---|
| 1 | Add Vehicle |
| 2 | Search Vehicle |
| 3 | Display All Vehicles |
| 4 | Display Parking Slots |
| 5 | Vehicle Exit |
| 6 | Update Vehicle |
| 7 | Delete Vehicle Record |
| 8 | Parking Statistics |
| 9 | Exit the Program |

## How It Works

1. **Vehicle registration:** The user enters the vehicle number, owner name, and vehicle type.
2. **Validation:** The system checks for an empty vehicle number and duplicate active/recorded vehicle numbers.
3. **Slot allocation:** The system assigns the first available parking slot.
4. **Record management:** Vehicle details are stored in a linked list.
5. **Vehicle exit:** The system records the exit time, calculates the parking fee, and releases the parking slot.
6. **Statistics:** The system displays the number of records, parked and exited vehicles, available slots, and recorded revenue.

## Parking Fee Calculation

The example implementation uses these rates per started hour:

| Vehicle Type | Rate |
|---|---:|
| Car | ₹50 |
| Bike | ₹20 |
| Scooter | ₹15 |
| Truck | ₹100 |

A minimum charge of one hour applies. The fee is calculated by rounding the parking duration up to the next hour. Rates can be changed in the `parking_rates` dictionary in the source code.

## Data Structures and Complexity

Let **n** be the number of vehicle records and **s** the number of parking slots.

| Operation | Expected Time Complexity | Explanation |
|---|---|---|
| Search vehicle | O(n) | May inspect every linked-list node |
| Insert vehicle record | O(n) | Traverses to the end of the linked list |
| Delete vehicle record | O(n) | Searches for the target node |
| Find available slot | O(s) | May inspect every parking slot |
| Display all vehicles | O(n) | Visits every vehicle record |

## Limitations

- Data is stored in memory and is lost when the program closes.
- The application uses a console interface.
- Parking rates and the number of slots are configured in the code.
- The current example does not include a database, persistent storage, or authentication.
- A waiting-queue class can be added or integrated if queue-based waiting management is required.

## Future Enhancements

- Save records permanently using SQLite or MySQL
- Add a graphical user interface (GUI)
- Add administrator login and role-based access
- Generate receipts and daily reports
- Add vehicle number-plate recognition or QR-based entry
- Integrate a dedicated FIFO queue for vehicles waiting for a slot

## Learning Outcomes

This project demonstrates:

- Classes, objects, constructors, and methods in Python
- Encapsulation of vehicle and parking operations
- Linked-list insertion, searching, and deletion
- Dictionary-based parking-slot tracking
- Basic algorithm analysis and time complexity
- Input validation and menu-driven program design

## Author

**Vaibhav Yadav**

## License

This project is intended for educational and demonstration purposes. Add a license file if you plan to distribute it under a specific open-source license.


