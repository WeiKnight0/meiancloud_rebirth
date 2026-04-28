from django import forms


class CommentForm(forms.Form):
    title = forms.CharField(
        label="标题",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "标题"}),
        required=True,
    )
    content = forms.CharField(
        label="评论",
        max_length=200,
        widget=forms.Textarea(
            attrs={
                "class": "textarea",
                "placeholder": "评论",
                "rows": 5,
                "style": "width: 100%; padding: 10px;border: 1px solid #ddd;border-radius: 4px;font-size: 1rem; resize:none;font-family:Arial, sans-serif;",
            }
        ),
    )


class ReplyForm(forms.Form):
    reply_content = forms.CharField(
        label="评论",
        max_length=200,
        widget=forms.Textarea(
            attrs={
                "class": "textarea",
                "placeholder": "回复",
                "rows": 5,
                "style": "resize:none;width:98%;font-family:Arial, sans-serif;",
            }
        ),
    )
