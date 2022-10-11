from  rest_framework import  serializers
from  article import  models
from django.contrib.auth.models import User


class UserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        firlds = [
            'id',
            'username',
            'last_name',
            'first_name',
            'email',
            'last_login',
            'date_joined'
        ]

class UserRegisterSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail',lookup_field='username')

    class Meta:
        model = User
        fields = ['url','username','password','is_superuser']
        extra_kwargs = {
            'password':{'write_only':True},
            'is_superuser' : {'read_only': True}
        }

    def create(self, validated_data):

        return  User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        print('UserRegisterSerializers  update方法执行了')
        if 'password' in validated_data:
            print('UserRegisterSerializers  update方法   验证执行了')
            password = validated_data.pop('password')
            print('UserRegisterSerializers  update方法得到密码'+password)
            instance.set_password(password)
        return  super().update(instance,validated_data)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','last_login','date_joined']
