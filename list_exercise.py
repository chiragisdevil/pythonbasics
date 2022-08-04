# 3-4 Guest List
guest_list = ["Krsna", "Anurag Kashyap", "Aradhya Walia"]
print(f"You are invited for dinner {guest_list[0]}, {guest_list[1]} and {guest_list[2]}")

# 3-5 Guest cannot make it
guest_declined = "Anurag Kashyap"
print(f"{guest_declined} cannot make it to dinner")

new_guest = "John Terry"
guest_list[1] = new_guest
print(f"You are invited for dinner {guest_list[0]}, {guest_list[1]} and {guest_list[2]}")

# 3-6 Bigger List
print("I have found a bigger table for the dinner")
bigger_guest_list = guest_list
bigger_guest_list.insert(0,"Tapsi Walia")
bigger_guest_list.insert(3,"Ajit Walia")
bigger_guest_list.append("Amyra Walia")
print(f"You are invited for dinner {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]}")

# 3-7 Shrinking list
print("Apologies, but I can only invite 2 people for the dinner")
removed_name = bigger_guest_list.pop()
print(f"I'm sorry {removed_name}, I cannot invite you for dinner")

removed_name = bigger_guest_list.pop()
print(f"I'm sorry {removed_name}, I cannot invite you for dinner")

removed_name = bigger_guest_list.pop()
print(f"I'm sorry {removed_name}, I cannot invite you for dinner")

removed_name = bigger_guest_list.pop()
print(f"I'm sorry {removed_name}, I cannot invite you for dinner")
print(f"you are invited for the dinner {bigger_guest_list[0]} and {bigger_guest_list[1]}")

print(f"I am inviting {len(bigger_guest_list)} people")

del bigger_guest_list[1]
del bigger_guest_list[0]
print(bigger_guest_list)