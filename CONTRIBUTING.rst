.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/arslanrafique/horizon_dashboard_boilerplate/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Horizon Dashboard Boilerplate could always use more documentation, whether as part of the
official Horizon Dashboard Boilerplate docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/arslanrafique/horizon_dashboard_boilerplate/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `horizon_dashboard_boilerplate` for local development.

1. Fork the `horizon_dashboard_boilerplate` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/horizon_dashboard_boilerplate.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv horizon_dashboard_boilerplate
    $ cd horizon_dashboard_boilerplate/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. Activate plugin via openstack_dashboard settings.py::

  In settings.py add following:

    import horizon_dashboard_boilerplate
    horizon_dashboard_boilerplate_path = os.path.dirname(horizon_dashboard_boilerplate.__file__)

  Now Add plugin in INSTALLED_APPS:

    [..., 'horizon_dashboard_boilerplate']

  Finally, Add templates support in TEMPLATES's DIR:

    'DIR' : [ ..., horizon_dashboard_boilerplate_path]

6. Copy files from enabled folder to openstack_dashboard/enabled folder::

  Great, restart Apache/Django server and you should see the changes.

7. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, 3.4 and 3.5, and for PyPy. Check
   https://travis-ci.org/arslanrafique/horizon_dashboard_boilerplate/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::


    $ python -m unittest tests.test_horizon_dashboard_boilerplate
