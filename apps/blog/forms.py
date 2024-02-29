from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'image', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-30',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-30',
            'id': 'email',
            'name': 'email',
            'placeholder': 'E-mail'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control mb-30',
            'id': 'image',
            'name': 'image',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control w-10',
            'id': 'content',
            'placeholder': "Write Content",
            'name': 'content',
            # 'cols': 30,
            # 'rows': 7,
        })