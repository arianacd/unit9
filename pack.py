import dog


class Pack:

    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0

    def get_leader_name(self):
        leader = self.members[self.leader_index]
        return leader.get_name()
