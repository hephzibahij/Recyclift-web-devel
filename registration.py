class Recycler:
    def __init__(self, name, address, estimated_weight):
        self.name = name
        self.address = address
        self.estimated_weight = estimated_weight

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"House Address: {self.address}")
        print(f"Estimated Weight of Recycled Bottles: {self.estimated_weight} kg")

def register_recycler():
    print("Welcome to the Recycler Registration Portal!")
    name = input("Enter your name: ")
    address = input("Enter your house address: ")
    estimated_weight = float(input("Enter the estimated weight of recycled bottles (in kg): "))

    recycler = Recycler(name, address, estimated_weight)
    print("\nRegistration Complete!")
    recycler.display_info()

if __name__ == "__main__":
    register_recycler()
