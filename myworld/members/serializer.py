from rest_framework import serializers
import re
from .models import Members

def validate_firstname(received_firstname):
        pattern = '^[a-zA-Z0-9]*$'  
        test_string = received_firstname
        result = re.match(pattern, test_string)
        if result:
            print("In serializers......")
            return received_firstname
        else:
            print("Not valid.....")
            raise serializers.ValidationError("Enter username with only Alphanumeric characters")

class MembersSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length = 20, validators = [validate_firstname])
    class Meta:
        model = Members
        fields = ['firstname', 'lastname']
        
          

