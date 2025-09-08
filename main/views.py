from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'THUNDR clubs',
        'name': 'Jessica Tandra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
