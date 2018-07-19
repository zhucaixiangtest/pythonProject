from rest_framework import serializers

from ApiSoftware.modes.login_models import tbl_user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = tbl_user
        fields = ('user_name', 'emal', 'phone', 'password', 'token_value', 'status')

