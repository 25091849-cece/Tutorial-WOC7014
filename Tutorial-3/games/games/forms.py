from django import forms

from games.models import Game, Review, Tags


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "developer", "platform", "label_tag"]
        widgets = {
            "label_tag": forms.CheckboxSelectMultiple,
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["game", "review"]
        widgets = {
            "review": forms.Textarea(attrs={"rows": 5}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ["label"]


