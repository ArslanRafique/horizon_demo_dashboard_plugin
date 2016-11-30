from django import conf
from django.utils.translation import ugettext_lazy as _

from horizon import tabs

class BoilerPlateTab(tabs.Tab):
    name = _("BoilerPlate Tab")
    slug = "boilerplate_tab"
    template_name = "horizon_dashboard_boilerplate/boilerplate_panel/index.html"

    def get_context_data(self, request):
        return {}

class BoilerPlateTabsGroup(tabs.TabGroup):
    slug = "boilerplate_tabs_group"
    tabs = (BoilerPlateTab,)
