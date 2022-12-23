from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
<<<<<<< HEAD

=======
>>>>>>> 36e39ec65a891b0aed2f584048d2a80ac00210b4

class userform(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
