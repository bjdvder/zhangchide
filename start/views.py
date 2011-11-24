from djangomako.shortcuts import render_to_response, render_to_string

def index(request):
    return render_to_response('index.html', {})
