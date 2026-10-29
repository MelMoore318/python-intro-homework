# Warmup 2: Student Dictionary

# Create a dictionary representing a student
student = {
    "name" : "Melanie",
    "grade" : "10th",
    "subjects" : ["Math", "Science", "History", "English"], 
}

# Print each key-value pair using .items()
for key, value in student.items():
  print(f"{key}: {value}")

  # Add a new key called graduated
student["graduated"] = False

# Print the updated dictionary
print("Updated dictionary:", student)