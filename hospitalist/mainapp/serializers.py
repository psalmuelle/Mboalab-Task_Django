from django.contrib.auth.models import User
from .models import HospitalDetail
from rest_framework import serializers


class HospitalDetailSerializer(serializers.Serializer):

    OWNERSHIP_CHOICES = (
        ("None", "None"),
        ("Private", "Private"),
        ("Public", "Public"),
        ("Non-Profit", "Non-Profit"),
    )

    FACILITY_LEVEL_CHOICES = (
        ("None", "None"),
        ("Primary", "Primary"),
        ("Secondary", "Secondary"),
        ("Tetiary", "Tetiary"),
    )

    FACILITY_TYPE_CHOICES = (
        ("None", "None"),
        ("General", "General"),
        ("Specialist", "Specialist"),
        ("Teaching", "Teaching"),
    )

    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    hospital_name = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length=200)
    region = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=1000)
    website_url = serializers.URLField()
    email = serializers.EmailField()
    hotline = serializers.CharField(max_length=15)
    operating_hours = serializers.CharField(max_length=50)
    ownership = serializers.ChoiceField(choices=OWNERSHIP_CHOICES)
    facility_level = serializers.ChoiceField(choices=FACILITY_LEVEL_CHOICES)
    facility_type = serializers.ChoiceField(choices=FACILITY_TYPE_CHOICES)
    services_offered = serializers.CharField(max_length=30000)
    bed_spaces = serializers.IntegerField()
    other_facilities = serializers.CharField(max_length=30000)

    def create(self, validated_data):
        return HospitalDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.user = validated_data.get("user", instance.user)
        instance.email = validated_data.get("email", instance.email)
        instance.hospital_name = validated_data.get("hospital_name", instance.hospital_name)
        instance.country = validated_data.get("country", instance.country)
        instance.region = validated_data.get("region", instance.region)
        instance.city = validated_data.get("city", instance.city)
        instance.address = validated_data.get("address", instance.address)
        instance.website_url = validated_data.get("website_url", instance.website_url)
        instance.hotline = validated_data.get("hotline", instance.hotline)
        instance.operating_hours = validated_data.get(
            "operating_hours", instance.operating_hours
        )
        instance.ownership = validated_data.get("ownership", instance.ownership)
        instance.facility_level = validated_data.get(
            "facility_level", instance.facility_level
        )
        instance.facility_type = validated_data.get(
            "facility_type", instance.facility_type
        )
        instance.services_offered = validated_data.get(
            "services_offered", instance.services_offered
        )
        instance.bed_spaces = validated_data.get("bed_spaces", instance.bed_spaces)
        instance.other_facilities = validated_data.get(
            "other_facilities", instance.other_facilities
        )

        instance.save()
        return instance
