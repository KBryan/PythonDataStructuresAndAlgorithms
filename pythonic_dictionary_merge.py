name = {'first_name' :  'Kwame', 'last_name': 'Bryan'}
job = {'company': 'Kwame Bryan Consulting', 'role':'Software Developer'}
contact = {'twitter','@elijahnomad', 'Github', 'www.github.com/KBryan'}

profile = {}
profile.update(name)
profile.update(job)
contact.update(contact)

print("Pythonic Dictionary Merge Example:")
print(profile)