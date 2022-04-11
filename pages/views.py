from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class TeamPageView(TemplateView):
    template_name = "team.html"

class PrimePageView(TemplateView):
    template_name = "prime.html"

class ServicesPageView(TemplateView):
    template_name = "services.html"

class bloodDonationPageView(TemplateView):
    template_name = "bloodDonation.html"

class EmergencyPageView(TemplateView):
    template_name = "emergency.html"

class CancellationPageView(TemplateView):
    template_name = "cancellation.html"

class privacyPolicyPageView(TemplateView):
    template_name = "privacyPolicy.html"

class DeliveryPageView(TemplateView):
    template_name = "delivery.html"

class temporaryHomePageView(TemplateView):
    template_name = "temporaryHome.html"