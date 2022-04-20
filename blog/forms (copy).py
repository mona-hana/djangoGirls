

from .models import Post

from blog.newForm.html 


class PostForm(forms):

    class Meta:
        model = Post
        fields = ('title', 'text',)
