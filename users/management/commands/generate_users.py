from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from faker import Faker
from datetime import date, timedelta
import random
from users.models import CustomUser

BATCH_SIZE = 1000
TOTAL = 10000

DEPARTMENTS = ["IT", "HR", "Sales", "Finance"]
ROLES = ["admin", "manager", "employee"]

fake = Faker()

def random_birth_date(start_year=1975, end_year=2005):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))

class Command(BaseCommand):
    help = "Generate users"

    def handle(self, *args, **options):
        users = []
        password_hash = make_password("12345")
        now = timezone.now()

        for i in range(TOTAL):
            first = fake.first_name()
            last = fake.last_name()
            email = fake.unique.email()
            username = (first + last + str(random.randint(1,9999)))[:150]
            phone = fake.phone_number()
            city = fake.city()
            country = fake.country()
            department = random.choice(DEPARTMENTS)
            role = random.choice(ROLES)
            birth = random_birth_date()
            salary = random.randint(200000, 1000000)

            user = CustomUser(
                email=email,
                username=username,
                first_name=first,
                last_name=last,
                phone=phone,
                city=city,
                country=country,
                department=department,
                role=role,
                birth_date=birth,
                salary=salary,
                is_active=True,
                is_staff=(role == "admin"),
                date_joined=now,
                last_login=None,
                password=password_hash
            )
            users.append(user)

            if len(users) >= BATCH_SIZE:
                CustomUser.objects.bulk_create(users)
                users = []

        if users:
            CustomUser.objects.bulk_create(users)