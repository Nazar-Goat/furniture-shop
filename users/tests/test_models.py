from django.contrib.auth import get_user_model
from django.test import TestCase

User= get_user_model()
class UserModelTest(TestCase):
    def test_create_user(self):
        user= User.objects.create_user(
            username= "user",
            first_name= "test_name",
            last_name= "test_surname",
            email= "test_email@gmail.com",
            phone_number= "1231231234",
            password= "testpass123"    
        )

        self.assertEqual(str(user), "user")
        self.assertEqual(user.phone_number, "1231231234")
        self.assertEqual(user.email, "test_email@gmail.com")