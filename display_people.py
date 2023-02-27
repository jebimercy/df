from main import People

my_people = People.select()
for person in my_people:
    print(People.name, People.phone, People.email, People.password, People.gender, People.religion, People.county)