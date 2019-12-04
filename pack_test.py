import pack
import dog

my_dog = dog.Dog("Piper")
my_dog2 = dog.Dog("Shamu")

my_pack = pack.Pack(my_dog)
print(my_pack.get_leader_name())
my_pack.add_member(my_dog2)
my_pack.print_pack()
print(my_pack.new_leader(1))
print(my_pack.get_leader_name())
