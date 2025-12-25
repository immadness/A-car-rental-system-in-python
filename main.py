class CarRentalSystem:
    def __init__(self):
        # Define car types and models
        self.car_types = ['Hatchbacks', 'Sedans', 'SUVs']
        self.car_models = {
            'Hatchbacks': ['Honda Civic', 'Peugeot208', 'Dacia Sandero', 'Hyundai i10', 'Volkswagen Polo', 'Volkswagen Golf', 'Ford Focus', 'Toyota Corolla', 'Skoda Octavia', 'Kia Picanto'],
            'Sedans': ['Kia Rio', 'Nissan Versa', 'Honda Civic Si', 'Hyundai Elantra N', 'Mazda 3','Volkswagen Jetta GLI', 'Honda Accord', 'Hyundai Sonata', 'Kia K5', 'Audi A3', 'Audi S3', 'Genesis G70'],
            'SUVs': ['Skoda Kodiaq', 'Volvo XC40', 'Audi Q5', 'Volkswagen T-cross', 'Kia EV6', 'Audi Q4 e-tron', 'Land Rover Defender', 'BMW X3', 'Nissan Juke', 'Dacia Sandero Stepway']
        }

        # Define rental prices
        self.prices = {
            'Hatchbacks': {'1-6 days': 30, '7+ days': 25, 'VIP': 20},
            'Sedans': {'1-6 days': 50, '7+ days': 40, 'VIP': 35},
            'SUVs': {'1-6 days': 100, '7+ days': 90, 'VIP': 80}
        }

        # Initialize rented cars and customer list
        self.rented_cars = {car_type: {model: [] for model in models} for car_type, models in self.car_models.items()}
        self.customers = ["ben dover", "lou sirr", "jack ingof", "Kratos"]

    def display_available_cars(self):
        for car_type in self.car_types:
            print(f"\nAvailable {car_type}:")
            for model in self.car_models[car_type]:
                if model not in self.rented_cars[car_type][model]:
                    print(f"- {model}")

    def rent_car(self, customer_name, car_type, car_model, days, is_vip=False):
        if car_type in self.car_types and car_model in self.car_models[car_type]:
            rental_price = self.prices[car_type]['VIP' if is_vip else ('7+ days' if days >= 7 else '1-6 days')]
            
            print(f"\nRenting {car_model} ({car_type}) for {days} days by {customer_name}.")
            print(f"Total cost: ${rental_price * days}")

            # Move rented car to customer's rented cars list
            self.rented_cars[car_type][car_model].append(customer_name)

            # Add customer to the list if not already present
            if customer_name not in self.customers:
                self.customers.append(customer_name)
        else:
            print("Invalid car type or model.")

    def return_car(self, customer_name, car_type, car_model):
        if car_type in self.car_types and car_model in self.car_models[car_type]:
            if customer_name in self.rented_cars[car_type][car_model]:
                print(f"\nReturning {car_model} ({car_type}) by {customer_name}.")
                # Remove the car from the customer's rented cars list
                self.rented_cars[car_type][car_model].remove(customer_name)
            else:
                print("Customer did not rent this car.")
        else:
            print("Invalid car type or model.")

    def display_rented_cars(self):
        print("\nRented Cars:")
        for car_type in self.car_types:
            for model, customers in self.rented_cars[car_type].items():
                if customers:
                    print(f"\n{car_type} - {model}:")
                    for customer in customers:
                        print(f"- {customer}")

class CustomersInquiry:
    def __init__(self, car_rental_system):
        self.car_rental_system = car_rental_system

    def inquire_about_car_types(self):
        print("\nCar Types and Prices:")
        for car_type in self.car_rental_system.car_types:
            print(f"\n{car_type}:")
            for duration, price in self.car_rental_system.prices[car_type].items():
                print(f"{duration}: ${price}")


# Example usage:
if __name__ == "__main__":
    rental_system = CarRentalSystem()
    inquiry_system = CustomersInquiry(rental_system)

    while True:
        print("\n1. Rent a car")
        print("2. Return a rented car")
        print("3. Display available cars")
        print("4. Display rented cars")
        print("5. Inquire about car types and prices")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            customer_name = input("Enter your name: ")
            car_type = input("Enter car type (Hatchbacks, Sedans, SUVs): ")
            car_model = input("Enter car model: ")
            days = int(input("Enter rental duration (in days): "))
            is_vip = input("Are you a VIP member? (yes/no): ").lower() == 'yes'

            rental_system.rent_car(customer_name, car_type, car_model, days, is_vip)

        elif choice == '2':
            customer_name = input("Enter your name: ")
            car_type = input("Enter car type (Hatchbacks, Sedans, SUVs): ")
            car_model = input("Enter car model: ")

            rental_system.return_car(customer_name, car_type, car_model)

        elif choice == '3':
            rental_system.display_available_cars()

        elif choice == '4':
            rental_system.display_rented_cars()
        
        elif choice == '5':
            inquiry_system.inquire_about_car_types()

        elif choice == '6':
            print("Exiting the car rental system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
