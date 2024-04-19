import requests
import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from datamap.forms import SubmitAPIForm, DatamapLineEditForm
from datamap.models import Datamap, DatamapLine


def home_view(request, *args, **kwargs):
    return redirect(reverse("dbasik_api"))


def dbasik_api_view(request):
    if request.method == 'POST':
        form = SubmitAPIForm(request.POST, request.FILES)
        if form.is_valid():
            url = 'http://localhost:4000/v1/datamaps'
            data = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
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
                        dm = Datamap.objects.create(name=data["datamap"]["name"],
                                                    description=data["datamap"]["description"])
                        for line in data["datamap"]["datamap_lines"]:
                            DatamapLine.objects.create(dm=dm, key=line["key"], sheet=line["sheet"],
                                                       cellref=line["cellref"])
                    messages.success(request, 'Data Map Created')
                    return redirect('datamap-list')
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


def datamaps_list_view(request):
    datamaps_list = Datamap.objects.all()
    context = {
        'datamaps_list': datamaps_list

    }
    return render(request, 'datamap_list.html', context)


def datamap_detail_view(request, pk):
    datamap = Datamap.objects.get(pk=pk)
    datamap_lines = DatamapLine.objects.filter(dm=datamap)
    context = {
        "datamap_lines": datamap_lines
    }
    return render(request, 'datamap_detail.html', context)


def datamap_line_edit(request, pk):
    datamap_line = DatamapLine.objects.get(pk=pk)
    context = {
        "datamap_line": datamap_line,
    }
    if request.method == "POST":
        form = DatamapLineEditForm(request.POST, instance=datamap_line)
        context["form"] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Line in datamap changed')
            return redirect('datamap-detail', pk=datamap_line.dm.pk)
        else:
            return render(request, 'datamap_line_edit.html', context)
    else:
        context["form"] = DatamapLineEditForm(instance=datamap_line)
        return render(request, 'datamap_line_edit.html', context)
