from unittest import skip
from django.test import TestCase
from django.urls import reverse, resolve
from datamap.forms import SubmitAPIForm
from datamap.models import Datamap, DatamapLine
from datamap.views import (
    dbasik_api_view,
    datamaps_list_view,
    datamap_detail_view,
    datamap_line_edit
)


class TestModels(TestCase):
    def setUp(self):
        self.dm = Datamap.objects.create(name="Test name", description="Test description")

    def test_create_object(self):
        self.assertEquals(self.dm.name, "Test name")

    def test_create_datamaplines(self):
        dml = DatamapLine.objects.create(dm=self.dm, key="Key 1", sheet="Sheet 1", cellref="A10")
        self.assertEquals(dml.key, "Key 1")


class TestUrlsViews(TestCase):
    def setUp(self):
        self.dm = Datamap.objects.create(
            name='Test',
            description='Test description'
        )
        self.dml = DatamapLine.objects.create(
            dm=self.dm,
            key='Test Key',
            sheet='Test Sheet',
            cellref='A1'
        )

    def test_dbasik_api_url(self):
        url = reverse('dbasik_api')
        self.assertEquals(resolve(url).func, dbasik_api_view)

    def test_dbasik_api_view(self):
        response = self.client.get(reverse('dbasik_api'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dbasik_api.html')

    def test_datamaps_list_url(self):
        url = reverse('datamap-list')
        self.assertEquals(resolve(url).func, datamaps_list_view)

    def test_datamap_list_view(self):
        response = self.client.get(reverse('datamap-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datamap_list.html')

    def test_datamap_detail_url(self):
        url = reverse('datamap-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, datamap_detail_view)

    def test_datamap_detail_view(self):
        response = self.client.get(reverse('datamap-detail', kwargs={'pk': self.dm.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datamap_detail.html')

    def test_datamap_line_edit_url(self):
        url = reverse('datamap-line-edit', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, datamap_line_edit)

    def test_datamap_line_edit_view(self):
        response = self.client.get(reverse('datamap-line-edit', kwargs={'pk': self.dml.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datamap_line_edit.html')



# @skip("Failing test - not bothered at the moment")
class SubmitAPIFormTest(TestCase):
    def test_form_fields(self):
        form = SubmitAPIForm()
        self.assertIn('csv_file', form.fields.keys())

    # not working
    def test_form_valid(self):
        # csv_file = open(os.path.join(BASE_DIR, "datamap/tests/datamap.csv"), 'rb')
        csv_file = "datamap/tests/datamap.csv"
        form_files = {
            'csv_file': csv_file,
        }
        # form_data = {}
        form = SubmitAPIForm(
            # data=form_data,
            files=form_files
        )

        self.assertTrue(form.is_valid())
        # csv_file.close()

    # def test_form_invalid(self):
    #     form_data = {}
    #     form = SubmitAPIForm(data=form_data)
    #     self.assertFalse(form.is_valid())





