from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # except for id all the fields are included, this also takes list of fields
        # exclude = ['secure data'] # the field that is not to be displayed
        labels = {
            "user_name": "Your Name",
            "review_text": "Your review",
            "rating": "Your rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter shorter name!"
            }
        }