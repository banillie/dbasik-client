import requests
import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from dbasik_client.forms import SubmitAPIForm


def home_view(request, *args, **kwargs):
    return redirect(reverse("dbasik_api"))


def dbasik_api_view(request):
    if request.method == 'POST':
        form = SubmitAPIForm(request.POST, request.FILES)
        if form.is_valid():
            url = 'http://localhost:4000/v1/datamaps'
            data = {
                'name': 'bobbins',
                'description': 'This is a long description of the datamap.'
            }
            files = {
                'file': form.cleaned_data['csv_file']
            }
            try:
                response = requests.post(url, data=data, files=files)
                if response.status_code == 200:
                    with open('/tmp/dm.json', 'wb') as f:
                        f.write(response.content)
                    with open('/tmp/dm.json', 'r') as file:
                        # Load JSON data into a Python dictionary
                        data = json.load(file)
                        print(data)
                    messages.success(request, 'Data Map Created')
                    return redirect('dbasik_api')
                else:
                    return render(
                        request,
                        'dbasik_api.html',
                        {'error_message': 'Failed to upload CSV file to API'}
                    )
            except requests.RequestException as e:
                messages.warning(request, 'Network Error. Try again')
                return redirect('dbasik_api')
    else:
        form = SubmitAPIForm()

    return render(request, 'dbasik_api.html', {'form': form})
