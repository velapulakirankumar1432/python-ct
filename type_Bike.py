class Bike:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed
    def display(self):
        print(self.brand, self.color, self.speed, "km/h")
    def accelerate(self, inc):
        self.speed += inc
        print("Speed after accelerating:", self.speed)
    def brake(self, dec):
        self.speed = max(0, self.speed - dec)
        print("Speed after braking:", self.speed)
b1 = Bike("Honda", "Red", 50)
b1.display()
b1.accelerate(20)
b1.brake(30)
b1.display()
