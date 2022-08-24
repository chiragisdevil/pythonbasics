# motorcycles = ["honda","yamaha","suzuki"]
# motorcycles[2] = "ducati"
# motorcycles.append("Royal Enfield")
# motorcycles.insert(0,"Pulsar")

# print(motorcycles)

# # removed_motorcycle = motorcycles.pop(0)

# del motorcycles[0]

# print(motorcycles)

# motorcycles.remove("ducati")

# print(motorcycles)

# 1) Assignment
# 2) Append & Insert
# 3) del command, pop method (with or without position)

# students = ["aradhya","Manya","Anshuman","Uday"]
 
# students[2] = "sanvi"

# students.append("amyra")
# print(students)

# students.insert(4,"vaishnavi")

# print(students)

# del students[2]
# print(students)

# removed_student = students.pop()
# print(students) 
# print(removed_student.title())

# removed_student2 = students.pop(2)
# print(students) 
# print(removed_student2.title())

# students.insert(1,"Amyra")
# print(students)

# students[0] = students[0].title()
# students[1] = students[1].title()
# students[2] = students[2].title()
# students[3] = students[3].title()
# print(students)

# students.remove("Manya")
# students.remove("Vaishnavi")
# print(students)

# Guest List
guest_list = ["Bhakti","Bhavya", "Komal"]
print(guest_list)
print(f"Hello {guest_list[0]}, I would like to invite you for kids playdate.")
print(f"Hello {guest_list[1]}, I would like to invite you for kids playdate")
print(f"Hello {guest_list[2]}, I would like to invite you for kids playdate")
print(f"Hello all {guest_list[2]} won't be able to make it for dinner")
guest_list[2] = "Mumma"
print(guest_list)
print(f"Hello {guest_list[2]}, I would like to invite you for kids playdate.")
print(f"Hello {guest_list[1]}, I would like to invite you for kids playdate.")
print(f"Hello {guest_list[0]}, I would like to invite you for kids playdate.")
print(f"Hello all I am inviting more people as I found a bigger space")
guest_list.insert(0,"Shruti")
guest_list.insert(2,"Geetika")
guest_list.append("Asmita")
print(guest_list)
print(f"Hello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]} Gentle Reminder to attend kids playdate on coming Sunday.")
print(f"Aplogies Now dinner table is avaiable just for 2 adults and 2 kids.")
removed_guest = guest_list.pop(0)
print(f" Aplogies {removed_guest} I can't invite you for a party")
# guest_list.pop(0)
removed_guest2 = guest_list.pop(0)
print(f"Aplogies {removed_guest2} I can't invite you for a party")
# guest_list.pop(0)
removed_guest3 = guest_list.pop(0)
print(f"Aplogies {removed_guest3} I can't invite you for a party")
guest_list.pop(0)
print(guest_list)
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)



