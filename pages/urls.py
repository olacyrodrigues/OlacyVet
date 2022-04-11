from django.urls import path

from .views import AboutPageView, HomePageView, TeamPageView, PrimePageView, ServicesPageView, bloodDonationPageView, EmergencyPageView, CancellationPageView, privacyPolicyPageView, DeliveryPageView, temporaryHomePageView

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("team/", TeamPageView.as_view(), name="team"), 
    path("prime/", PrimePageView.as_view(), name="prime"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("bloodDonation/", bloodDonationPageView.as_view(), name="bloodDonation"),
    path("emergency/", EmergencyPageView.as_view(), name="emergency"),
    path("cancellation/", CancellationPageView.as_view(), name="cancellation"),
    path("privacyPolicy/", privacyPolicyPageView.as_view(), name="privacyPolicy"),
    path("delivery/", DeliveryPageView.as_view(), name="delivery"),
    path("temporaryHome/", temporaryHomePageView.as_view(), name="temporaryHome"),
    
]