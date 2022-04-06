from django.shortcuts import render
from django.utils.translation import gettext as _  # 1

# Create your views here.
def index(request):
    if request.LANGUAGE_CODE == 'en-us':
        return render(request, 'join/index-en.html')
    else:
        context_dict = { 
            'localize_key': _('I am localized inside the view.') 
        }
        return render(request, 'join/index.html', context_dict)

def switch_lang(request):
    return render(request, 'join/parts/langswitch.html')
