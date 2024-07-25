# news/management/commands/populate_news.py

from django.core.management.base import BaseCommand
from faker import Faker
import random
from a_news.models import News


class Command(BaseCommand):
    help = 'Populate the News model with random data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        categories = ['capital', 'nation', 'politics', 'global',
                      'stock', 'sports', 'science_tech', 'weather']

        for _ in range(15):
            title = faker.sentence(nb_words=6)
            author = faker.name()
            published_date = faker.date_time_this_year()
            image = faker.image_url()
            content = faker.text(max_nb_chars=2000)
            category = random.choice(categories)

            news = News(
                title=title,
                author=author,
                published_date=published_date,
                image=image,
                content=content,
                category=category,
            )
            news.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the News model with random data'))
