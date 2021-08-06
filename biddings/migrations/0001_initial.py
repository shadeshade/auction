# Generated by Django 3.2.5 on 2021-08-05 18:09

import biddings.tools
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BiddingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='item_images')),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('auction_starts_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('auction_ends_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_sold', models.BooleanField(default=False)),
                ('purchaser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_items', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_items', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, biddings.tools.ResizeImageMixin),
        ),
    ]
