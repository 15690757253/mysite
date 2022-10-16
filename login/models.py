from django.db import models


class User(models.Model):

    gender = {
        ('male', "男"),
        ('female', "女"),
    }

    name = models.CharField(max_length=16, verbose_name="用户名", unique=True, db_column='name', default=None)
    password = models.CharField(max_length=256, verbose_name="密码",  default=None)
    email = models.EmailField(unique=True, verbose_name="邮箱", default=None)
    sex = models.CharField(max_length=8, choices=gender, default="男", verbose_name="性别")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    has_confirmed = models.BooleanField(default=False)

    # 人性化显示对象
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        # 指定表名
        db_table = 'user'
        verbose_name = "用户表"
        verbose_name_plural = "用户表"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"