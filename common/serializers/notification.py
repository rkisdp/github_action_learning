from rest_framework import serializers
from common.models import Notification


class NotificationSerializers(serializers.ModelSerializer):

    def validate(self, data):
        data['user_id'] = self.context['request'].user.id
        return data

    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('id', 'user')
        datetime_fields = ('create_date', 'modified_date')

