from faker import Faker

fake = Faker()

for _ in range(5):
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print()
