from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2"]


class AboForm(forms.Form):
    """form for the abo page, to follow and unfollow users"""

    search = forms.CharField(max_length=50, label=False)

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_search(self):
        search = self.cleaned_data["search"]

        # impossible to follow yourself:
        if self.user and self.user.username == search:
            raise forms.ValidationError("You can not follow yourself!")

        # impossible to follow an admin/superuser:
        if UserModel.objects.filter(username=search, is_superuser=True).exists():
            raise forms.ValidationError("Please choose an other name to follow!")

        return search
