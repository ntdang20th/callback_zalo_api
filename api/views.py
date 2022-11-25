from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/zalo_verifierNE6YEzl4C3jQqBSCcgSzBrYwfXQqnNTADJ8.html')