from djangomako.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {})

def dart_notwork(request):
    return render_to_response('dart_notwork.html', {})

def dart_sunflower(request):
    return render_to_response('dart_sunflower.html', {})

def dart_slider(request):
    return render_to_response('dart_slider.html', {})