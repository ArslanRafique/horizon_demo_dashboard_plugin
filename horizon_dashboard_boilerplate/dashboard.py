from django.utils.translation import ugettext_lazy as _

import horizon

class BoilerPlatePanelGroup(horizon.PanelGroup):
    slug = "boilerplate_panel_group"
    name = _('BoilerPlate Panel Group')
    panels = ('boilerplate_panel')


class BoilerPlateDashboard(horizon.Dashboard):
    name = _("BoilerPlate Dashboard")
    slug = "boilerplate_dashboard"
    panels = (BoilerPlatePanelGroup,)
    default_panel = 'boilerplate_panel' #TODO: create panel


horizon.register(BoilerPlateDashboard)
