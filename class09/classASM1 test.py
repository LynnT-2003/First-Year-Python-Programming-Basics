def MyBio(name,  surname,  age):
    if age < 5 or age > 70:
        return (f"Dear {name} {surname}, you should stay home to avoid Covid-19.")
    else:
        return (f'Dear {name} {surname}, please stay home as much as you can.')

print (MyBio('lynn', 'thit', 18))
