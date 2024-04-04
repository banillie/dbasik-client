import os
from django.test import TestCase
from django.urls import reverse, resolve
from dbasik_client.settings import BASE_DIR
from dbasik_client.views import dbasik_api_view
from dbasik_client.forms import SubmitAPIForm


class TestUrls(TestCase):
    def test_dbasik_api_url(self):
        url = reverse('dbasik_api')
        self.assertEquals(resolve(url).func, dbasik_api_view)

    def test_dbasik_api_view(self):
        response = self.client.get(reverse('dbasik_api'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dbasik_api.html')


class SubmitAPIFormTest(TestCase):
    def test_form_fields(self):
        form = SubmitAPIForm()
        self.assertIn('csv_file', form.fields.keys())

    # not working
    def test_form_valid(self):
        csv_file = open(os.path.join(BASE_DIR, "dbasik_client/tests/datamap.csv"), 'rb')
        form_files = {
            'csv_file': csv_file,
        }
        form_data = {}
        # Instantiate the form with the form data
        form = SubmitAPIForm(data=form_data, files=form_files)

        # Check if the form is valid
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    # def test_form_invalid(self):
    #     form_data = {}
    #     form = SubmitAPIForm(data=form_data)
    #     self.assertFalse(form.is_valid())





