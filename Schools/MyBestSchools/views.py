from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "products": [
            {
                "name": "Хліб",
                "count" : 100
            },
            {
            "name": "Сіль",
            "count": 50
        },
        {
            "name": "Молоко",
            "count": 30
        },
    ]}
    return render(request=request, template_name="index.html", context=context)