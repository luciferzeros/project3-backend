from rest_framework import serializers
from ..models.deliveryaddress import DeliveryAddress
import re
r = re.compile(r'^\d{0}?(0|9)\d{9}$')


class DeliveryAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryAddress
        fields = ['id', 'user', 'phone', 'address', 'default']

    def validate(self, attrs):
        if not r.search(attrs.get("phone")):
            raise serializers.ValidationError({"message": "Số điện thoại không hợp lệ"})
        return attrs


class UpdateDeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ['default']

    def update(self, instance, validated_data):
        dellivery_address = DeliveryAddress.objects.filter(user=instance.user, on_delete=False)
        for del_add in dellivery_address:
            del_add.default = False
            del_add.save()
        instance.default = True
        instance.save()
        return instance


class DeleteDeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ['on_delete']

    def update(self, instance, validated_data):
        instance.on_delete = True
        instance.save()
        if instance.default == True:
            dellivery_address = DeliveryAddress.objects.filter(user=instance.user, on_delete=False).last()
            dellivery_address.default = True
            dellivery_address.save()
        return instance