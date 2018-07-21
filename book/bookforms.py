from book.models import Author, Book, AuthorDetail, Publish
from django.core.exceptions import ValidationError  # 导入验证错误
from django import forms  # 导入forms组件
from django.forms import widgets  # HTML Widget classes


# author校验规则
class AuthorForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=32,
                           error_messages={'required': '该字段不能为空', 'max_length': '不能超过32个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           )
    age = forms.IntegerField(min_value=1, max_value=200, label="年龄",
                             error_messages={'required': '该字段不能为空', 'invalid': '年龄格式错误','min_value': '年龄不能小于0', 'max_value': '年龄不能大于200'},
                             widget=widgets.NumberInput(attrs={'class': 'form-control'}),
                             )
    birthday = forms.DateTimeField(label="生日", error_messages={'required': '该字段不能为空'},
                                   widget=widgets.TextInput(attrs={'type': 'date', 'class': 'form-control'}))

    telephone = forms.IntegerField(label="电话",
                                   widget=widgets.TextInput(attrs={'class': 'form-control'}),
                                   error_messages={'required': '该字段不能为空', 'invalid': '电话格式错误'},
                                   )
    address = forms.CharField(label="地址",
                              error_messages={'required': '该字段不能为空', },
                              widget=widgets.TextInput(attrs={'class': 'form-control'}),
                              )

    # 验证手机号
    def clean_telephone(self):
        val = self.cleaned_data.get("telephone")
        if len(str(val)) == 11:
            return val
        else:
            raise ValidationError("请输入11位手机号")


class PublishForm(forms.Form):
    name = forms.CharField(label="名称", max_length=32,
                           error_messages={'required': '该字段不能为空', 'max_length': '不能超过32个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           )
    city = forms.CharField(label="地址",
                           error_messages={'required': '该字段不能为空', },
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           )
    email = forms.EmailField(label="邮箱",
                             error_messages={'required': '该字段不能为空', 'invalid': '邮箱格式错误'},
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}),
                             )


class BookForm(forms.Form):

    def get_choice(obj):
        """得到select框的所有choices"""
        obj_list = []
        for item in obj:
            obj_list.append((item.id, item.name))
        return tuple(obj_list)

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    publish_choice = get_choice(publish_list)
    author_choice = get_choice(author_list)

    title = forms.CharField(label="书名", max_length=32,
                            error_messages={'required': '该字段不能为空', 'max_length': '不能超过32个字符'},
                            widget=widgets.TextInput(attrs={'class': 'form-control'}),
                            )
    price = forms.DecimalField(label="价格", max_digits=8, decimal_places=2,
                               widget=widgets.NumberInput(attrs={'class': 'form-control'}),
                               error_messages={'required': '该字段不能为空', 'invalid': '该字段格式错误'},
                               )
    pub_date = forms.DateField(label="出版日期", error_messages={'required': '该字段不能为空'},
                               widget=widgets.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    publish = forms.ChoiceField(label="出版社", choices=publish_choice,
                              error_messages={'required': '该字段不能为空', },
                              widget=widgets.Select(attrs={'class': 'form-control'}),
                              )
    authors = forms.MultipleChoiceField(label="作者", choices=author_choice,
                              error_messages={'required': '该字段不能为空', },
                              widget=widgets.SelectMultiple(attrs={'class': 'form-control'}),
                              )
