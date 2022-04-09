from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'links': {
            'github': 'https://github.com/givntek',
            'vinted': 'https://www.vinted.fr/',
            'rakuten': 'https://shopping.rakuten.com/'
        }
    }
    return render(request, 'index.html', context)

def join(request):
    return render(request, 'join.html')

def contribute(request):
    return render(request, 'contribute.html')

def docs(request):
    return render(request, 'docs.html')

def getHelp(request):
    context = {
        'matrixurl': 'https://matrix.to/#/#givntek:matrix.org'
    }
    return render(request, 'get-help.html', context)


def activitypub(request):
    return render(request, 'docs/activitypub.html')

def permissions(request):
    return render(request, 'docs/permissions.html')

def developers(request):
    return render(request, 'docs/developers.html')

def translations(request):
    return render(request, 'docs/translations.html')

def customize(request):
    return render(request, 'docs/customize.html')

def production(request):
    return render(request, 'docs/production.html')

def updating(request):
    return render(request, 'docs/updating.html')

def images(request):
    return render(request, 'docs/images.html')

def docker(request):
    return render(request, 'docs/docker.html')

def switch_lang(request):
    return render(request, 'parts/langswitch.html')
