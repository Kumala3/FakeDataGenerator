import faker

fake = faker.Faker()

data = {
    "name": fake.name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "address": fake.address().replace("\n", ", "),
    "social_media": fake.url(),
}

print(data)
