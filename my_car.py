class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return str("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        super().__init__(model, color, mpg)
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"


my_car = Car(model="DeLorean", color="silver", mpg=88)
print('Model: ', my_car.model)
print(my_car.condition)
print('Drive')
my_car.drive_car()
print(my_car.condition)
my_car = ElectricCar(model="Tesla", color="red", mpg=0, battery_type="molten salt")
print('Model: ', my_car.model, 'Battery: ', my_car.battery_type)
my_car.drive_car()
print(my_car.condition)
