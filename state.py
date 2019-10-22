import math


class State:
    description = ""
    length = 0
    radian = False
    start = 0
    valuetype = ''
    visible = False
    value = None

    def __init__(self, Description, Length, Radian, Start, ValueType, Visible):
        self.description = Description
        self.length = Length
        self.radian = Radian
        self.start = Start
        self.valuetype = ValueType
        self.visible = Visible

    def __str__(self):
        if self.radian == 'True':
            return "{}: \t {}".format(self.description, self.truncate(math.degrees(self.value), 4))
        else:
            return "{}: \t {}".format(self.description, self.truncate(self.value, 4))

    def truncate(self, number, digits) -> float:
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper
