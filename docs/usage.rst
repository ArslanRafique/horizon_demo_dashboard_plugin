=====
Usage
=====

To use Horizon Dashboard Boilerplate in a project::

1. Activate plugin via openstack_dashboard settings.py::

  In settings.py add following:

    import horizon_dashboard_boilerplate
    horizon_dashboard_boilerplate_path = os.path.dirname(horizon_dashboard_boilerplate.__file__)

  Now Add plugin in INSTALLED_APPS:

    [..., 'horizon_dashboard_boilerplate']

  Finally, Add templates support in TEMPLATES's DIR:

    'DIR' : [ ..., horizon_dashboard_boilerplate_path]

2. Copy files from enabled folder to openstack_dashboard/enabled folder::

  Great, restart Apache/Django server and you should see the changes.
