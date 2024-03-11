from faker import Faker

fake = Faker()

oot = "oot"

def get_registered_user():
    return {
        "name": oot,
        "speed": fake.random_int(50, 200),
    }


if __name__ == "__main__":
    print(get_registered_user())