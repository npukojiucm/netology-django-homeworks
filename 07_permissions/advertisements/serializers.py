from pprint import pprint

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # Обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # Само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        method = self.context["request"].method

        if method == 'POST':
            user = self.context['request'].user
            count_open_adv = Advertisement.objects.filter(creator=user, status='OPEN').count()

            if count_open_adv >= 10:
                raise ValidationError('There can be no more than 10 open ads')

        if method == 'PATCH':
            pk_adv = self.context['request'].parser_context['kwargs'].get('pk')
            status_adv = Advertisement.objects.get(id=pk_adv).status

            if status_adv == 'OPEN' == data['status']:
                raise ValidationError('This ad is already open')

        return data
