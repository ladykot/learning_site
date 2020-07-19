from faker import Faker

fake = Faker(locale='ru_RU')

for num in range(3):
    print(fake.first_name())