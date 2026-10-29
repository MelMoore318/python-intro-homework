# Warmup 3: Set Operations

# Create two hardcoded lists of programming languages
languages1 = ["Python", "Java", "C++", "JavaScript"]
languages2 = ["Java", "C#", "Python", "Ruby"]

# Convert each list to a set
set1 = set(languages1)
set2 = set(languages2)

# Print the union (all languages, no duplicates)
print("Union of languages:", set1.union(set2))

# Print the intersection (languages in both sets)
print("Intersection of languages:", set1.intersection(set2))

# Print the difference (languages only in the first set)
print("Difference of languages (set1 - set2):", set1.difference(set2))