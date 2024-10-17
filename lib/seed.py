from pet import Pet
from owner import Owner

print("deleting rows")
Pet.delete_all()
Owner.delete_all()


print('creating rows')
john = Owner.create(name="John")
bob = Owner.create(name="Bob")
sarah = Owner.create(name="Sarah")

Pet.create(name="Garfield", species="Cat", owner_id=john.id)
Pet.create(name="Odi", species="Dog", owner_id=john.id)
Pet.create(name="Milo", species="Cat", owner_id=sarah.id)
Pet.create(name="Otis", species="Dog", owner_id=sarah.id)
Pet.create(name="Toby", species="Dog", owner_id=bob.id)
Pet.create(name="Tweety", species="Bird")

print("done seeding")