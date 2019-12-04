import dog


class Pack:

    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0
        self.members.append(dog)

    def get_leader_name(self):
        leader_dog = self.members[self.leader_index]
        return leader_dog.get_name()

    def add_member(self, dog_two):
        self.members.append(dog_two)

    def print_pack(self):
        print("the pack contains:")
        for member in self.members:
            print(member.get_name())

    def new_leader(self, index):

        leader_dog = self.members[index]
        self.leader_index = index
        return leader_dog.get_name()


