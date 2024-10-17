
from pet import Pet
from owner import Owner
from globals import clear, space, any_key_to_continue, invalid_choice

class Cli():
  def start(self):
    clear()
    print("Welcome to the Pet Shop!")
    self.main_menu()

  # MENU METHODS

  def restart_main_menu(self):
      any_key_to_continue()
      clear()
      self.main_menu()

  def restart_pet_details(self, pet):
      any_key_to_continue()
      clear()
      self.print_pet_details(pet)
      self.pet_details_menu(pet)

  def restart_owner_details(self, owner):
      any_key_to_continue()
      clear()
      self.print_owner_details(owner)
      self.owner_details_menu(owner)

  def main_menu(self):
    space()
    print("Type '1' to list Owners")
    print("Type '2' to list Pets")
    print("Type '3' to create an Owner")
    print("Type '4' to create a Pet")
    print("Type '5' to select an owner")
    print("Type '6' to select a pet")
    print("Type 'exit' to exit program")
    space()
    self.main_menu_selection()

  def pet_details_menu(self, pet):
    space()
    print(f"Type '1' to edit {pet.name}")
    print(f"Type '2' to delete {pet.name}")
    print("Type '3' to get adopted")
    print("Type 'main' to exit to main menu")
    space()
    self.pet_details_menu_selection(pet)

  def pet_details_menu_selection(self, pet):
    user_input = input("Enter Here: ")
    if user_input == "1":
      clear()
      print("editing pet")
      self.restart_pet_details(pet)
    elif user_input == "2":
      clear()
      print("deleting pet")
      self.restart_pet_details(pet)
    elif user_input == "3":
      clear()
      print("being adopted")
      self.restart_pet_details(pet)
    elif user_input == "main":
      clear()
      print("going back to main menu")
    else:
      clear()
      invalid_choice()
      self.restart_pet_details(pet)

  def owner_details_menu(self, owner):
    space()
    print(f"Type '1' to edit {owner.name}")
    print(f"Type '2' to delete {owner.name}")
    print("Type '3' to adopt a pet")
    print("Type 'main' to exit to main menu")
    space()
    self.owner_details_menu_selection(owner)

  def owner_details_menu_selection(self, owner):
    user_input = input("Enter Here: ")
    if user_input == "1":
      clear()
      print("editing owner")
      self.restart_owner_details(owner)
    elif user_input == "2":
      clear()
      print("deleting owner")
      self.restart_owner_details(owner)
    elif user_input == "3":
      clear()
      print("adopt a pet")
      self.restart_owner_details(owner)
    elif user_input == "main":
      clear()
      print("going back to main menu")
    else:
      clear()
      invalid_choice()
      self.restart_owner_details(owner)

  def main_menu_selection(self):
    user_input = input("Enter Here: ")
    if user_input == "1":
      clear()
      self.list_owners()
      self.restart_main_menu()

    elif user_input == "2":
      clear()
      self.list_pets()
      self.restart_main_menu()
    elif user_input == "3":
      clear()
      self.create_owner()
      self.restart_main_menu()
    elif user_input == "4":
      clear()
      self.create_pet()
      self.restart_main_menu()
    elif user_input == "5":
      clear()
      self.select_owner()
      self.restart_main_menu()
    elif user_input == "6":
      clear()
      self.select_pet()
      self.restart_main_menu()
    elif user_input == "exit":
      clear()
      print("exiting program, goodbye")
    else:
      clear()
      invalid_choice()
      self.restart_main_menu()

  def list_owners(self):
    print("Owner List")
    print("----------")
    i = 1
    for owner in Owner.all():
      self.print_owner(owner, i)
      i = i + 1
    
  def print_owner(self, owner, list_number):
    print(f"{list_number}. {owner.name}")

  def print_owner_details(self, owner):
    print(f"{owner.name} Details")
    print("----------")
    space()
    print(f"Name: {owner.name}")
    space()
    print("Pets:")
    self.print_owner_pets(owner)

  def print_pet_details(self, pet):
    print(f"{pet.name} Details")
    print("----------")
    space()
    print(f"Name: {pet.name}")
    space()
    print(f"Species: {pet.species}")
    space()
    print(f"Owner: {pet.owner().name if pet.owner() else 'Not adopted'}")
    
  
  def print_owner_pets(self, owner):
    i = 1
    for pet in owner.pets():
      self.print_pet(pet, i)
      i = i + 1

  def list_pets(self):
    print("Pet List")
    print("----------")
    i = 1
    for pet in Pet.all():
      self.print_pet(pet, i)
      i = i + 1
    
  def print_pet(self, pet, list_number):
    print(f"{list_number}. {pet.name}")

  def create_owner(self):
    print("Create Owner")
    print("----------")
    space()
    owner_name = input("Enter Name: ")
    Owner.create(name=owner_name)
    clear()
    print("Owner Successfully created")

  def create_pet(self):
    print("Create Pet")
    print("----------")
    space()
    pet_name = input("Enter Name: ")
    species = input("Enter Species: ")
    Pet.create(name=pet_name, species=species)
    clear()
    print("Pet Successfully created")

  def select_owner(self):
    print("Select Owner")
    print("----------")
    space()
    user_input = input("Enter number associated with owner: ")
    try:
      index = int(user_input) - 1
      owners = Owner.all()
      length_of_owners = len(owners)
      if index in range(0, length_of_owners):
        owner = owners[index]
        clear()
        self.print_owner_details(owner)
        self.owner_details_menu(owner)
      else:
        clear()
        invalid_choice()
    except ValueError as error:
      clear()
      invalid_choice()

  def select_pet(self):
    print("Select Pet")
    print("----------")
    space()
    user_input = input("Enter number associated with pet: ")
    try:
      index = int(user_input) - 1
      pets = Pet.all()
      length_of_pets = len(pets)
      if index in range(0, length_of_pets):
        pet = pets[index]
        clear()
        self.print_pet_details(pet)
        self.pet_details_menu(pet)
      else:
        clear()
        invalid_choice()
    except ValueError as error:
      clear()
      invalid_choice()