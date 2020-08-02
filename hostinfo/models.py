from django.db import models


class Server(models.Model):
    """服务器设备"""
    sub_asset_type_choice = (
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机'),
    )
    created_by_choice = (
        ('auto', '自动添加'),
        ('manual', '手工录入'),
    )
    # Create your models here.
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice,
                                              default=0, verbose_name="服务器类型")
    created_by = models.CharField(choices=created_by_choice, max_length=32,
                                  default='auto', verbose_name="添加方式")
    hosted_on = models.ForeignKey('self', related_name='hosted_on_server',
                                  blank=True, null=True, verbose_name="宿主机",
                                  on_delete=models.CASCADE)  # 虚拟机专用字段
    IP = models.CharField('IP地址', max_length=30, default='')
    MAC = models.CharField('Mac地址', max_length=200, default='')
    model = models.CharField(max_length=128, null=True, blank=True,
                             verbose_name='服务器型号')
    hostname = models.CharField(max_length=128, null=True, blank=True,
                                verbose_name="主机名")
    os_type = models.CharField('操作系统类型', max_length=64, blank=True,
                               null=True)
    os_distribution = models.CharField('发行商', max_length=64, blank=True,
                                       null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True,
                                  null=True)
def __str__(self):
    return '%s-%s' % (self.id, self.hostname)
class Meta:
    verbose_name = '服务器'
    verbose_name_plural = "服务器"