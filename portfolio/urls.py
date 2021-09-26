from django.urls import path
from portfolio.apis import testimonials

urlpatterns = [
    path(
        "testimonials/",
        testimonials.ListTestimonialsView.as_view(),
        name="testimonial_list_api"
    ),
]
