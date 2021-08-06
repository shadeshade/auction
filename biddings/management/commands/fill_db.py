import datetime

import factory
from dateutil.tz import UTC
from django.core.management.base import BaseCommand
from factory import fuzzy


class MyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.MyUser'

    username = factory.lazy_attribute(lambda x: f'{x.first_name}{x.last_name}')
    email = factory.lazy_attribute(lambda x: f'{x.username}.@test.com'.lower())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BiddingItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'biddings.BiddingItem'

    item_name = factory.Faker('name')
    description = factory.Faker('name')
    starting_bid = factory.fuzzy.FuzzyInteger(0, 999999)
    auction_starts_at = fuzzy.FuzzyDateTime(
        datetime.datetime(2009, 1, 1, tzinfo=UTC), datetime.datetime(2019, 1, 1, tzinfo=UTC))
    auction_ends_at = fuzzy.FuzzyDateTime(
        datetime.datetime(2019, 1, 1, tzinfo=UTC), datetime.datetime(2029, 1, 1, tzinfo=UTC))
    seller = factory.SubFactory(MyUserFactory)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(10):
            MyUserFactory()
            BiddingItemFactory()
