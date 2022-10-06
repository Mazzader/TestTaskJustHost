from django.db import models


class VPS(models.Model):
    STATUS_BLOCKED = 0
    STATUS_STARTED = 1
    STATUS_STOPPED = 2

    uid = models.AutoField(primary_key=True)
    cpu = models.SmallIntegerField(verbose_name='central processing unit')
    ram = models.SmallIntegerField(verbose_name='random access memory')
    hdd = models.IntegerField(verbose_name='hard disk drive')
    status = models.SmallIntegerField(
        verbose_name='status',
        choices=(
            (STATUS_BLOCKED, 'blocked'),
            (STATUS_STARTED, 'started'),
            (STATUS_STOPPED, 'stopped'),
        ),
        db_index=True,
    )

    class Meta:
        verbose_name = 'virtual dedicated server'
        verbose_name_plural = 'virtual dedicated servers'
