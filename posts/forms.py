from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=255, 
        help_text='Enter each tag separated by a comma and a space. eg. "tag1, tag2"'
        )
    text = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'author',
            'text',
            'publish',
            'status',
            'tags',

        ]

    def create_tags(self):
        tags_list = self.cleaned_data['tags'].split(',')
        post = super(PostForm, self).save()
        for tag in tags_list:
            tag_name = tag.strip()
            new_tag = Tag.objects.get_or_create(name=tag_name)[0]
            new_tag.posts.add(post.id)
            new_tag.save()
            

