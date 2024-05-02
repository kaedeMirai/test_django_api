from django.shortcuts import render


def navigations(request):
    """
    Представление для рендера домашней страницы с подключением к вебсокету.
    """
    return render(request, "home.html")


def ws_temp_view(request):
    """
    Представление для рендеринга страницы с подключением к вебсокету.
    """
    return render(request, 'ws_temp.html')
