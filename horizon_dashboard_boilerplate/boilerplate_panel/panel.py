import logging
from django.utils.translation import ugettext_lazy as _
import horizon

from horizon_dashboard_boilerplate import dashboard
from openstack_dashboard.api import base

class BoilerPlatePanel(horizon.Panel):
    name = _('BoilerPlate Panel')
    slug = "boilerplate_panel"


dashboard.BoilerPlateDashboard.register(BoilerPlatePanel)
