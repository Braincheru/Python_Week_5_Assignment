# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self._brand = brand  # Encapsulation: protected attribute
        self._model = model
        self._storage = storage
        self._battery_capacity = battery_capacity
        self._battery_level = 100  # Default battery level in percentage
        self._is_powered_on = False  # Default state
    
    # Method to turn on the phone
    def power_on(self):
        if not self._is_powered_on:
            self._is_powered_on = True
            print(f"{self._brand} {self._model} is now powered on.")
        else:
            print(f"{self._brand} {self._model} is already powered on.")
    
    # Method to turn off the phone
    def power_off(self):
        if self._is_powered_on:
            self._is_powered_on = False
            print(f"{self._brand} {self._model} is now powered off.")
        else:
            print(f"{self._brand} {self._model} is already powered off.")
    
    # Method to use battery
    def use_battery(self, usage):
        if self._is_powered_on and self._battery_level > 0:
            self._battery_level -= usage
            self._battery_level = max(self._battery_level, 0)
            print(f"Used {usage}% battery. Battery level: {self._battery_level}%.")
        elif not self._is_powered_on:
            print("Phone is powered off. Cannot use battery.")
        else:
            print("Battery is completely drained!")
    
    # Method to charge the battery
    def charge_battery(self, charge):
        self._battery_level += charge
        self._battery_level = min(self._battery_level, 100)
        print(f"Battery charged to {self._battery_level}%.")

    # Method to display phone details
    def display_details(self):
        print(f"Brand: {self._brand}, Model: {self._model}, Storage: {self._storage}GB, "
              f"Battery Capacity: {self._battery_capacity}mAh, Battery Level: {self._battery_level}%.")

# Subclass representing a Smartphone with advanced features
class SmartCameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, camera_megapixels):
        super().__init__(brand, model, storage, battery_capacity)
        self._camera_megapixels = camera_megapixels  # Additional feature
    
    # Polymorphism: Enhanced display details
    def display_details(self):
        super().display_details()  # Call base class method
        print(f"Camera: {self._camera_megapixels} MP")
    
    # Method specific to the subclass
    def take_photo(self):
        if self._is_powered_on and self._battery_level > 5:
            self.use_battery(5)  # Using 5% battery per photo
            print(f"Photo taken with {self._camera_megapixels} MP camera!")
        elif not self._is_powered_on:
            print("Cannot take photo. The phone is powered off.")
        else:
            print("Not enough battery to take a photo!")

# Example usage
if __name__ == "__main__":
    # Creating instances
    basic_phone = Smartphone("Nokia", "3310", 32, 1200)
    camera_phone = SmartCameraPhone("Samsung", "Galaxy S22", 256, 5000, 108)
    
    # Interacting with the basic phone
    basic_phone.display_details()
    basic_phone.power_on()
    basic_phone.use_battery(20)
    basic_phone.charge_battery(10)
    basic_phone.power_off()
    
    # Interacting with the camera phone
    camera_phone.display_details()
    camera_phone.power_on()
    camera_phone.take_photo()
    camera_phone.power_off()
