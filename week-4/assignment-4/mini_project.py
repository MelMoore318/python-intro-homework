# Week 4 Mini Project: Student Roster Analysis

# Student roster copied from roster.py
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Starting values for our calculations
top_score = -1
top_name = ""
total_score = 0
subjects = set()
high_scores = []

# Look at each student, one at a time
for student in students:
    name = student["name"]
    score = student["score"]
    subject = student["subject"]

  # Find the student with the highest score
    if score > top_score:
        top_score = score
        top_name = name

 # Add the score to the running total
    total_score += score

# Collect unique subjects
    subjects.add(subject)      

# Collect names of students scoring above 75
    if score > 75:
        high_scores.append(name)

# Calculate the class average
class_average = total_score / len(students)

# Print the results
print(f"Top scorer: {top_name} with a score of {top_score}")
print(f"Class average: {class_average:.2f}")
print(f"Subjects offered: {', '.join(subjects)}")
print(f"High scoring students (above 75): {', '.join(high_scores)}")