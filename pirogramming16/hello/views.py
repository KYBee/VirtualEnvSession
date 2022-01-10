from django.shortcuts import render

# Create your views here.
def hello(request):

    context = {
        "name" : "여러분들의 이름을 적으세요"
    }

    return render(request, template_name="hello.html", context=context)