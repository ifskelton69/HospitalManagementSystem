class HospitalManagementSystem:
    def __init__(self):
        self.users = {}
        self.patients = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists! Please choose another one.")
            return False
        self.users[username] = password
        print("Registration successful!")
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful!")
            return True
        print("Invalid username or password.")
        return False

    def add_patient(self, name, sex, age, address, contact):
        if name in self.patients:
            print("Patient with the same name already exists! Please enter a different name.")
            return False
        self.patients[name] = {"Sex": sex, "Age": age, "Address": address, "Contact": contact}
        print("Patient added successfully!")
        return True

    def show_patients(self):
        if not self.patients:
            print("No patients registered yet!")
            return
        print()
        print("List of Patients:")
        print("----------------------------------------------------------------------------------------------")
        for name, details in self.patients.items():
            print(f" Name: {name}\n Sex: {details['Sex']}\n Age: {details['Age']}\n Address: {details['Address']}\n Contact: {details['Contact']}")
            print("----------------------------------------------------------------------------------------------")

def main():
    hospital_system = HospitalManagementSystem()

    while True:
        print("""
        ================================
           Welcome To CityHospital
        ================================
        1. Sign In
        2. Registration
        3. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if hospital_system.login(username, password):
                while True:
                    print("""
                    1. Add New Patient
                    2. View Patients
                    3. Sign Out
                    """)
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        name = input("Enter patient's name: ")
                        sex = input("Enter patient's sex: ")
                        age = input("Enter patient's age: ")
                        address = input("Enter patient's address: ")
                        contact = input("Enter patient's contact: ")
                        hospital_system.add_patient(name, sex, age, address, contact)

                    elif user_choice == '2':
                        hospital_system.show_patients()

                    elif user_choice == '3':
                        print("Logged out successfully!")
                        break

        elif choice == '2':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            hospital_system.register_user(username, password)

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
