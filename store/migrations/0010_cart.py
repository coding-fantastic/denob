# Generated by Django 4.1.2 on 2022-10-11 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0009_servicemen_specialities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('menuitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.menuitem')),
                ('outlet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.outlets')),
                ('servicemen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.servicemen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
