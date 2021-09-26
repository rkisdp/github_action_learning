from rest_framework import serializers
from portfolio.models import Testimonial


class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
        datetime_fields = ('create_date', 'modified_date')
