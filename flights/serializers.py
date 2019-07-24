from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']


class RegistrationSerializer (serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password','last_name','first_name']

	def create(self, validated_data):
		u = validated_data['username']
		pwrd = validated_data['password']
		lnm = validated_data['last_name']
		fnm = validated_data['first_name']
		new_user = User(username=u, last_name = lnm, first_name = fnm)
		new_user.set_password(pwrd)
		new_user.save()
		return new_user



 