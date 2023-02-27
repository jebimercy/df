from main import People

try:
    people_name = input("Enter your name \n")
    people_phone = input("Enter your phone number \n")
    people_email = input("Enter your email \n")
    people_password = input("Enter password \n")
    people_gender = input("Enter your gender \n")
    people_religion = input("Which religion are your \n")
    people_county = input("Enter county \n")

    People.create(name=people_name, phone=people_phone, email=people_email, password=people_password, gender=people_gender, religion=people_religion, county=people_county)

    print("Successfully")

except:
    print("Not successful")
