from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blogue/post_list.html', {})
