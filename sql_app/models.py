from django.db import models

# Create your models here.

class User(models.Model):
    # 字段类型
    # AutoField 自增字段
    # IntegerField 整型
    # CharField 字符串类型
    # DateTimeField 日期时间类型
    # BooleanField 布尔类型
    # FloatField 浮点型
    # DecimalField 浮点型
    # TextField 长文本类型
    # DateField 日期类型
    # TimeField 时间类型
    # ImageField 图片类型
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    sex = models.IntegerField()
    age = models.IntegerField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # 模型配置
    class Meta:
        db_table = "demo_user"
        ordering = ["-id"]

    def __str__(self):
        return self.name + " " + str(self.age) + " " + str(self.sex) + " " + str(self.pub_time)