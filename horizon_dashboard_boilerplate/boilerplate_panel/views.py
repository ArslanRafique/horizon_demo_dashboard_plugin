
import json
from django.views import generic
from django.http import HttpResponse
from horizon import tabs
from horizon_dashboard_boilerplat.boilerplate_panel.tabs import BoilerPlateTabsGroup

class JSONView(generic.View):

    def get(self, request):
        dummy_data = {
            'name': 'Arslan',
            'profession': 'Development',
            'Likes': 'Python, Angular'
        }

        return HttpResponse(
            json.dumps(dummy_data),
            content_type="application/json")


class IndexView(tabs.TabView):
    tab_group_class = BoilerPlateTabsGroup
    template_name = 'horizon_dashboard_boilerplate/boilerplate_panel/index.html'
