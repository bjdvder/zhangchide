from djangomako.shortcuts import render_to_response

def index(request):
    return render_to_response('fun/index.html', {})

def dart(request):
    return render_to_response('fun/dart_index.html', {})

def dart_notwork(request):
    return render_to_response('fun/dart_notwork.html', {})

def dart_sunflower(request):
    return render_to_response('fun/dart_sunflower.html', {})

def dart_slider(request):
    return render_to_response('fun/dart_slider.html', {})

def hd(request):
    """happy day work"""
    return render_to_response('fun/hd.html', {})

def har_view(request):
    return render_to_response('fun/har_view.html', {})
