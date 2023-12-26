from django import forms

from posts_app.models import Post
from posts_app.utils.model_utils import check_attachment_extensions


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text", "attachment"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["attachment"].required = False

    def clean(self):
        cleaned_data = super().clean()
        attachment = cleaned_data.get("attachment")

        if attachment:
            try:
                check_attachment_extensions(attachment.name)
            except ValueError as e:
                self.add_error("attachment", str(e))

        return cleaned_data
