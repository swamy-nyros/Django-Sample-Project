from django import forms
from .models import Question, Post_Comment, File_Upload

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=300)

class PostCommentForm(forms.Form):
    new_comment = forms.CharField(max_length=300)


class FileUploadForm(forms.Form):    
    upload_file = forms.FileField(
        label='Select a file'
        )
