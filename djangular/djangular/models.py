from django.db import models
from rest_framework import serializers

CATEGORIES = (
    ('item1', 'item2'),
    ('item3', 'item4'),
    ('item5', 'item6'),
    ('item7', 'item8'),
    ('item9', 'item10')
)


class ItemToBuy(models.Model):
    category = models.TextField(choices=CATEGORIES)
    name = models.TextField()
    important = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ItemToBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemToBuy
        fields = ('id', 'category', 'name', 'important', 'created_on')
