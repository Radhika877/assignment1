import os,django,random
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ftl.settings")
django.setup()

from faker import Faker
from myapp.models import user,activity_periods
from django.contrib.auth.models import User
from django.utils import timezone

def create_post(N):
    fake = Faker()
    for _ in range(10):
        id = random.randint(1,10)
        real_name = fake.name()
        tz = random.choice(['America','Los Angeles','Asia','Kolkata'])
        Post.objects.create(title=real_name + "POST!!",
        real_name = User.objects.get(id=id),
        slug = "-".join(real_name),
        tz=fake.text(),
        created = timezone.now(),
        updated = timezone.now(),
        )
        
        
    create_post(10) 
    print('DATA HAS BEEN POPULATED')