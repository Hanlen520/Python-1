from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .managers import UserInheritanceManager, UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    email = models.EmailField(
        _('email address'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):

    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """

    # 姓名
    name = models.CharField(max_length=20, default='第一次登录')
    # 性别
    sex = models.CharField(max_length=3, default='男')
    # 8位数字
    birthday = models.CharField(max_length=20, default='1990-01-01')
    # 工号
    job_number = models.CharField(max_length=10, default='0001')    # 工号

    # 政治面貌
    zhengzhi_mianmao = models.CharField(max_length=10, default='群众')
    # 6位数字，入党、团时间
    zhengzhi_time = models.CharField(max_length=20, default='2010-01-01')

    # 职称
    job_title = models.CharField(max_length=30, default='工程师')
    # 活得职称的时间
    job_time = models.CharField(max_length=20, default='2011-01-01')

    # 职位
    job_name = models.CharField(max_length=30, default='员工')
    # 身份证号
    identity_number = models.CharField(max_length=30, default='612322198103040001')

    # 学历
    education_background = models.CharField(max_length=30, default='本科')
    # 毕业学校
    school = models.CharField(max_length=30, default='北京老干部学校')
    # 毕业时间
    graduate_time = models.CharField(max_length=20, default='2005-07-01')
    # 入职时间
    job_join_time = models.CharField(max_length=20, default='2005-07-01')
    # 所属部门
    team_belong = models.CharField(max_length=20, default='C919')

    # 手机号码
    phone_number = models.CharField(max_length=30, default='13200001234')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.name

    # def age(self):
    #     return birthday_filter(self.birthday)
