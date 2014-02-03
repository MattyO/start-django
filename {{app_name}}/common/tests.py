from django.test import TestCase
from django.http import HttpResponse
from common.helpers import jsonify, resolve_http_method
import json

from changeless.types import FancyHash

# Create your tests here.
class HelperTests(TestCase):
    def test_jsonify_helper(self):
        some_data = {"a_key": "some data"}
        http_response = jsonify(some_data)
        response_data = json.loads(http_response.content)
        self.assertEqual(response_data['a_key'], 'some data')

    def test_resolve_http_method_with_locals(self):
        fake_request = FancyHash({"method":"GET"})
        def get():
            return HttpResponse("hello there")

        response = resolve_http_method(fake_request, locals())
        self.assertEqual(response.content, "hello there")

    def test_resolve_http_method_with_list(self):
        fake_request = FancyHash({"method":"GET"})
        def get():
            return HttpResponse("hello there")

        response = resolve_http_method(fake_request, [get])
        self.assertEqual(response.content, "hello there")

    def test_resolve_http_method_with_dict(self):
        fake_request = FancyHash({"method":"GET"})

        def get():
            return HttpResponse("hello there")
        def real_get():
            return HttpResponse("real hello there")

        response = resolve_http_method(fake_request, {"get":real_get})
        self.assertEqual(response.content, "real hello there")

    def test_resolve_http_method_returns_501_when_method_not_found(self):
        fake_request = FancyHash({"method":"GET"})
        response = resolve_http_method(fake_request, locals())
        self.assertEqual(response.status_code, 501)
