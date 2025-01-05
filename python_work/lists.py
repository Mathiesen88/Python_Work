bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0]) # prints the first element in the list
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[-1]) # prints the last element in the list

print(bicycles[0].title()) # prints the first element in the list with title case

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # changes the first element in the list
print(motorcycles)

motorcycles.append('honda') # adds an element to the end of the list
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati') # inserts an element at the beginning of the list
print(motorcycles)

del motorcycles[0] # deletes the first element in the list
print(motorcycles)

del motorcycles[1] # deletes the second element in the list
print(motorcycles)

popped_motorcycle = motorcycles.pop() # removes the last element in the list
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati') # removes the element 'ducati' from the list
print(motorcycles)

removed_motorcycle = 'yamaha'
motorcycles.remove(removed_motorcycle)
print(motorcycles)
print(f"\nA {removed_motorcycle.title()} is too expensive for me.")

guest_list = ['james','john','jane','jill']
print(f"\nHello {guest_list[0].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[1].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[2].title()}, would you like to come to dinner?")

print(f"\n{guest_list[2].title()} can't make it to dinner.")
guest_list[2] = 'jerry'
print(f"\nHello {guest_list[0].title()}, would you like to come to dinner?")

print("\nI found a bigger dinner table.")
guest_list.insert(0,'jason')
guest_list.insert(2,'jim')
guest_list.append('joseph')
print(f"\nHello {guest_list[0].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[1].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[2].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[3].title()}, would you like to come to dinner?")

print("\nI can only invite two people to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest.title()}, I can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest.title()}, I can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest.title()}, I can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest.title()}, I can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest.title()}, I can't invite you to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)