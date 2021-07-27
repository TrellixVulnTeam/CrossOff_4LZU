from django.db import models
from common.models import User
import uuid


class Mandalart(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return str(self.user.nickname) + '의 만다라트'


class BigGoal(models.Model):
    manda = models.OneToOneField(Mandalart,
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    content = models.CharField(max_length=200)
    is_achieved = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.manda.user.nickname) + '의 큰 목표 ' + str(self.content)


class MidGoal(models.Model):
    big = models.ForeignKey(BigGoal,
                            on_delete=models.CASCADE,
                            related_name='biggoal')
    content = models.CharField(max_length=200)
    is_achieved = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.big.manda.user.nickname) + '의 ' + str(self.content)


class SpecificGoal(models.Model):
    mid = models.ForeignKey(MidGoal,
                            on_delete=models.CASCADE,
                            related_name='midgoal')
    content = models.CharField(max_length=200)
    is_achieved = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.mid.big.manda.user.nickname) + '의 ' + str(self.content)
