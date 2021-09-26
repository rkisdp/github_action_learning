from rest_framework.generics import ListAPIView
from portfolio.models import Testimonial
from portfolio.serializers.testimonials import TestimonialSerializers


class ListTestimonialsView(ListAPIView):
    model = Testimonial
    serializer_class = TestimonialSerializers

    def get_queryset(self):
        return self.model.objects.all()

