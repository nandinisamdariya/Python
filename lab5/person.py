person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if the person dictionary has skills key and print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills)//2] if len(skills) % 2 != 0 else skills[len(skills)//2 - 1]
print(middle_skill)

# II. Check if person has Python skill
has_python_skill = 'Python' in person['skills']
print(has_python_skill)

# III. Print title based on skills
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown title')

# IV. Check if the person is married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
