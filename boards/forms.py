from django import forms
from .models import Topic
from .models import Post
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs = {'row':5,'placeholder':'你心里在想什么呢?'}),   #添加属性，行数和占位符
        max_length=4000,
        help_text='The max length of the text is 4000'       #帮助信息
    )

    class Meta:
        model = Topic
        fields = ['subject','message']             #显示的字段

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]