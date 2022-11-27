from rest_framework import serializers 
from noteapp.models import Note


class Noteserializer(serializers.Serializer):
    title =serializers.CharField()
    body =serializers.CharField()
    date_created =serializers.DateTimeField()

    def put(self, instance , data ):
        instance.title = data.get('title',instance.title)
        instance.body = data.get('body',instance.body )

        instance.save()
        return instance


    def create(self, data):
        return Note.objects.create(**data)

        