# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubsciptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rafael Francischini',
            cpf='12345546451',
            email='rafinha.unix@gmail.com',
            phone='2188181811'
        )

    def test_create(self):
        'Subscription must have name,cpf,email,phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Rafael Francischini', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force the collision
        Subscription.objects.create(name="Rafael Francischini", cpf="12345678901",
                                    email="rafinha.unix@gmail.com", phone="818181818")

    #TEM QUE LEVANTAR EXCESSAO
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name="Rafael Francischini", cpf="12345678901",
                         email="outro@email.com", phone="1212211221")
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        s = Subscription(name="Rafael Francischini", cpf="dasasdsdsd",
                         email="rafinha.unix@gmail.com", phone="1212211221")
        self.assertRaises(IntegrityError, s.save)
