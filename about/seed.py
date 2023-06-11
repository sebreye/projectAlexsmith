from django_seed import Seed
from .models import About
from faker import Faker


def about_run():
    seeder = Seed.seeder()
    fake = Faker()
    for _ in range(1):
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        website = fake.url()
        phone = fake.phone_number()
        city = fake.city()
        age = fake.random_int(min=18, max=90)
        degree = fake.job()
        email = fake.email()
        freelance = fake.boolean()

        seeder.add_entity(About, 1, {
            'birthday': birthday,
            'website': website,
            'phone': phone,
            'city': city,
            'age': age,
            "degree": degree,
            'email': email,
            'freelance': freelance,
        })

    print(seeder.execute())