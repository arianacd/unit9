class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        self.trick_list.append("sit")
        print(self.name + " sit")

    def lay(self):
        self.trick_list.append("lay down")
        print(self.name + " lay down")

    def roll(self):
        self.trick_list.append("roll over")
        print(self.name + " roll over")

    def catch(self):
        self.trick_list.append("catch squirrels")
        print(self.name + " catch squirrels")

    def soccer(self):
        self.trick_list.append("play soccer")
        print(self.name + " go get the ball")

    def print_trick_list(self):
        if not self.trick_list:
            print(self.name + " has not performed any tricks yet.")
        else:
            print(self.name + " knows how to do the following tricks:")
            for x in self.trick_list:
                print(x)
