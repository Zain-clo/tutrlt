
class Car:
   
    def __init__(self, make, model, year):
        self.make = make     
        self.model = model  
        self.year = year      
        print(f"Car created: {self.year} {self.make} {self.model}")

  
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

   
    def __del__(self):
        print(f"Car destroyed: {self.year} {self.make} {self.model}")



if __name__ == "__main__":

    my_car = Car("Toyota", "Camry", 2020)


    my_car.display_info()

    # Deleting the car object to invoke the destructor
    del my_car

