from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/zalo_verifierJlQVCv_rBcuUW8fZsV0-GXFlXLR_a5G8Cp0.html')