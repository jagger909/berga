from urllib.request import urlopen
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.http import urlquote


class Zayavka(models.Model):
    class Meta():
        db_table = 'zayavka'

    zayavka_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    zayavka_text = models.TextField(max_length=100)

    def __str__(self):
        return self.name


def sms_send(msg):
    url = "http://sms.ru/sms/send?api_id=%(api_id)s&to=%(to)s&text=%(msg)s"
    id_api = "AFAA4570-8FEE-0ADA-7EBE-781D7A61B515"
    number = "9179354824"
    url = url % {'api_id': urlquote(id_api), 'to': urlquote(number), 'msg': urlquote(msg.encode('utf-8'))}
    res = urlopen(url)
    res = res.code

    # try:
    #   response = urlopen(url)

    # if response.code != 200:
    #   sms_logger = 'Falied send SMS: status %s - %s' % (response.code, response.read()))
    #  return False
    # except Exception as err:
    #   sms_logger.error('Falied send SMS: %s' % err)
    #   return False

    return 'SMS status: %s' % res
