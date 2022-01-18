from app.wsgi import *
from core.erp.models import Type

from django.test import TestCase


# a = Type.objects.create(name='mia')
# a.save()
#
# #traer alguien en especifico
# c = Type.objects.get(pk=1)
# print(c)

# y = Type.objects.get(pk=1)
# y.name = 'maria'
# y.save()

#mostrar all
t = Type.objects.all()
print(t)

# #eliminacion
# i = Type.objects.get(pk=1)
# i.delete()
