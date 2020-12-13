from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Clinic, Profile, Pharmacy
from django.core import serializers


@login_required
def update_location(request):

    try:
        user_profle = models.Profile.objects.get(user=request.user)
        if not user_profle:
            raise ValueError("Can't get User details")

        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)

        global user_location
        user_location = point
        user_profle.last_location = point
        user_profle.save()

        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@login_required
def pharmacy(request):
    return render(request, 'pharmacy.html')

@login_required
def maps(request):
    return render(request, 'maps.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Home(generic.ListView):
    model = Clinic
    context_object_name = 'clinics'
    model = Profile

    user_location = Point(-6.2488, 53.3338, srid=4326)
    # user_location = Profile.last_location

    queryset = serializers.serialize("json", Clinic.objects.annotate(distance=Distance('location',
                                                                    user_location)).order_by('distance')[0:6])

    template_name = 'home.html'


class Pharmacy(generic.ListView):
    model = Pharmacy
    context_object_name = 'pharmacies'
    model = Profile

    user_location = Point(-6.2488, 53.3338, srid=4326)
    # user_location = Profile.last_location

    queryset = serializers.serialize("json", Pharmacy.objects.annotate(distance=Distance('location',
    user_location)).order_by('distance')[0:6])

    template_name = 'pharmacy.html'


