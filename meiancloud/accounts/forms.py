from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import UserProfile


USER_GENDER_TYPE = UserProfile.USER_GENDER_TYPE


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户",
        max_length=32,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "用户名"}),
    )
    password = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "密码"}),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        min_length=6,
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "用户名只能包含字母、数字和下划线"}
        ),
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9_]+$",
                message="用户名只能包含字母、数字和下划线",
                code="invalid_username",
            )
        ],
    )
    password = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "密码"}),
    )
    password1 = forms.CharField(
        label="再次输入密码",
        min_length=6,
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "再次输入密码"}
        ),
    )
    nick_name = forms.CharField(
        label="昵称",
        max_length=32,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "昵称"}),
    )
    email = forms.EmailField(
        label="邮箱",
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "邮箱"}),
    )
    gender = forms.ChoiceField(
        choices=UserProfile.USER_GENDER_TYPE,
        label="性别",
        initial="0",
        widget=forms.Select(attrs={"class": "input-gender"}),
    )
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "input input-birthday", "type": "date"}
        ),
        label="出生日期",
        required=False,
    )

    def clean_username(self):
        # 注册阶段先做基础唯一性校验，避免无意义创建用户。
        username_get = self.cleaned_data.get("username")
        exists = User.objects.filter(username=username_get).exists()
        if exists:
            raise forms.ValidationError("用户名已存在")
        if str(username_get) == "":
            raise forms.ValidationError("用户名不能为空")
        return username_get

    def clean_password1(self):
        # 第二次密码输入用于确认，不单独保存。
        password_get = self.cleaned_data.get("password")
        password1_get = self.cleaned_data.get("password1")
        if password_get != password1_get:
            raise forms.ValidationError("两次输入的密码不一致！")
        return password1_get

    def clean_gender(self):
        # 表单默认值只是占位项，提交时必须选择真实性别。
        gender_get = self.cleaned_data.get("gender")
        if gender_get == "0":
            raise forms.ValidationError("请选择性别！")
        return gender_get


class UserProfileForm(forms.Form):
    nick_name = forms.CharField(label="昵称", max_length=20, required=True)
    gender = forms.ChoiceField(label="性别", choices=USER_GENDER_TYPE, required=True)
    birthday = forms.DateField(
        label="出生日期", widget=forms.DateInput(attrs={"type": "date"}), required=True
    )
    sign = forms.CharField(
        label="个性签名", max_length=100, required=False, widget=forms.Textarea
    )
    image = forms.ImageField(label="头像", required=False)

    ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}
    MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2MB

    def __init__(self, *args, **kwargs):
        userprofile = kwargs.pop("userprofile", None)
        super().__init__(*args, **kwargs)
        if userprofile is None:
            raise ValueError("UnknownError")
        # 编辑表单直接回填当前资料，模板无需重复拼接初始值。
        self.fields["nick_name"].initial = userprofile.nick_name
        self.fields["gender"].initial = userprofile.gender
        self.fields["birthday"].initial = str(userprofile.birthday).replace("/", "-")
        self.fields["sign"].initial = userprofile.sign

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image
        if image.content_type not in self.ALLOWED_CONTENT_TYPES:
            raise forms.ValidationError("仅支持 JPG、PNG、GIF、WebP 格式")
        if image.size > self.MAX_IMAGE_SIZE:
            raise forms.ValidationError("图片不能超过 2MB")
        return image


class ChangePasswordForm(forms.Form):
    old = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "原密码"}),
    )
    new1 = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "新密码"}),
    )
    new2 = forms.CharField(
        label="密码",
        min_length=6,
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "再次输入新密码"}
        ),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_old(self):
        # 修改密码前必须先验证旧密码。
        old_password = self.cleaned_data.get("old")
        if not authenticate(username=self.user.username, password=old_password):
            raise forms.ValidationError("旧密码不正确")
        return old_password

    def clean_new2(self):
        # 在第二次输入阶段完成新密码一致性校验。
        new1 = self.cleaned_data.get("new1")
        new2 = self.cleaned_data.get("new2")
        if new1 and new2 and new1 != new2:
            raise forms.ValidationError("两次输入的密码不一致")
        return new2
