student = {
    'first_name': 'Nandini',
    'last_name': 'Samdariya',
    'gender': 'Female',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'India',
    'city': 'Kolkata',
    'address': 'Howrah-06'
}

# I. Get the length of the student dictionary
student_len = len(student)
print(student_len)

# II. Get the value of skills and check its data type
skills = student.get('skills', [])
skills_type = type(skills)
print ( skills , skills_type)

# III. Modify the skills by adding one or two skills
student['skills'].extend(['Flutter', 'React'])

# IV. Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)

# V. Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

# VI. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)

# VII. Delete one of the items in the dictionary
student.pop('address')
print(student)

# VIII. Delete the dictionary
del student
