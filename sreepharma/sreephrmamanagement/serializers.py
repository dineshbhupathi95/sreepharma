from rest_framework.serializers import ModelSerializer
from .models import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def Emailsendserializer(**data):
    mail_subject = "USER RESPONCE"
    print(data)
    print(data['first_name'])
    contentmessage = render_to_string('user_mail', {
        'first_name': data['first_name']
    })
    send_mail(mail_subject,contentmessage,"bupathidinesh@gmail.com",[data["email"],])
    return "success"
class usersinformationserializer(ModelSerializer):

    class Meta:
        model = Userinfromation
        fields = "__all__"

    def create(self, validated_data):
        Emailsendserializer(**validated_data)
        return Userinfromation.objects.create(**validated_data)

