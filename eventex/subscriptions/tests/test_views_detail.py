# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailsTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Rafael Francischini', cpf='12345678901',
                                        email='rafinha.unix@gmail.com', phone='21-96186180')
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'GET /inscricao/1/ should status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses Template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check in subscription data was rendered'
        self.assertContains(self.resp, 'Rafael Francischini')

class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)