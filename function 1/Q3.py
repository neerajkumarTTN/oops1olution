class Vehicle:
    def __init__(self,no_of_wheels,current_speed=0):
        self.no_of_wheels=no_of_wheels
        self.current_speed=current_speed
    def start(self):
        pass
    def stop(self):
        pass
    def accelerate(self):
        self.current_speed+=10
        return self.current_speed
    def brake(self):
        self.current_speed-=10
        if self.current_speed<0:
            self.current_speed=0
        return self.current_speed
car=Vehicle(4)
print(f"After Accelerating the car speed: {car.accelerate()}")
print(f"After apply the brake speed:{car.brake()}")
bike=Vehicle(2,50)
print(f"After accelerating the bike speed:{bike.accelerate()}")
print(f"After apply the brake :{bike.brake()}")