import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
import pandas as pd
from tablib import Dataset
from django.shortcuts import get_object_or_404


def index(request):

    return render(request, 'index.html', {})
    """View function for home page of site.

    model = Shoe

    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    # Render the HTML template index.html with the data in the context variable


def feminine_shoes(request):

    # Render the HTML template feminine_shoes.html with the data in the context variable
    return render(request, 'feminine_shoes.html', {})

def masculine_shoes(request):

    # Render the HTML template feminine_shoes.html with the data in the context variable
    return render(request, 'masculine_shoes.html', {})

class ShoeListView(generic.ListView):
    model = Shoe

def feminine_shoe_detail_view(request, primary_key):

    shoe = get_object_or_404(Shoe, pk=primary_key)

    return render(request, '')

# one parameter named request
def read_csvfile(request):

    tmp_data=pd.read_csv('src/data.csv',sep=',')
    #ensure fields are named~ID,Product_ID,Name,Ratio,Description
    #concatenate name and Product_id to make a new field a la Dr.Dee's answer
    shoes = [
        Shoe(
            id=tmp_data.ix[row][0],
            name=tmp_data.ix[row][1],
            price=tmp_data.ix[row][2],
            size=tmp_data.ix[row][3],
            style=tmp_data.ix[row][4],
            type=tmp_data.ix[row][5],
            color=tmp_data.ix[row][6],
            brand=tmp_data.ix[row][7],
            post_date=tmp_data.ix[row][8],
            status=tmp_data.ix[row][9],
        )
        for row in tmp_data['ID']
    ]
    Shoe.objects.bulk_create(shoes)

    # declaring template
    template = "read_csvfile.html"
    data = Shoe.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be id, name, price, size, style, type, color, brand, post_date, status',
        'shoes': data
              }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['src/data.csv']

    # Checking if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Shoe.objects.update_or_create(
            id=column[0],
            name=column[1],
            price=column[2],
            size=column[3],
            style=column[4],
            type=column[5],
            color=column[6],
            brand=colum[7],
            post_date=colum[8],
            status=colum[9]
        )
    context = {}
    return render(request, template, context)

"""
