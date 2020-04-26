from django import forms
from .models import Student


# 逐个字段的定义Form中的字段
# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEAM)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.EmailField(label='邮件', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手机', max_length=128)

# 直接调用models.py中的字段，并且校验qq号码是否是数字

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = ('name', 'sex', 'profession', 'email', 'qq', 'phone')
