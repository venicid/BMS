from django.contrib.auth.models import User  # auth_user表对象
from django.core.exceptions import ValidationError  # 导入验证错误
from django import forms  # 导入forms组件
from django.forms import widgets   # HTML Widget classes


# 定义校验规则
class UserForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=10, label="用户名",
                           error_messages={'required': '该字段不能为空', 'min_length': '不能少于4个字符', },
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),  # html控件添加样式
                           )
    password = forms.CharField(min_length=4, label="密码",
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                          error_messages={'required': '该字段不能为空', 'min_length': '不能少于4个字符',},
                          )
    r_password = forms.CharField(label="确认密码",
                            error_messages={'required': '该字段不能为空',},
                            widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                            )
    email = forms.EmailField(label="邮箱",
                             error_messages={'required': '该字段不能为空', 'invalid': '格式错误'},
                             widget=widgets.EmailInput(attrs={'class': 'form-control'})
                             )

    # 直接覆盖父类的clean方法， 全局钩子
    def clean(self):
        password = self.cleaned_data.get("password")
        r_password = self.cleaned_data.get("r_password", " ")
        # 先判断是否接受到pwd，r_pwd的值
        if password and r_password:
            if password == r_password:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data

    # 验证用户名
    def clean_username(self):
        val = self.cleaned_data.get("username")     # 获取清洗后的字段中的name

        ret = User.objects.filter(username=val)  # 数据库中的user
        if not ret:
            return ret
        else:
            raise ValidationError('该用户已经注册')    # 验证错误


