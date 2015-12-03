.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

Introduction
============

crgis.theme offers theme resources for the `CRGIS project`_.

.. _CRGIS project: http://crgis.rchss.sinica.edu.tw/about

Installation
============

This package is tested with Plone 4.3.2+ environment.
The easiest way is to use Plone 4.3.x UnifiedInstaller to get started.
Add this line in the eggs section of your ``buildout.cfg``::

    [buildout]

    ...

    eggs =
        ...
        crgis.theme

And then run "bin/buildout".

Copyright and License
=====================

`CRGIS (Culture Resource Geographic Information System)`_ is developed and run
by `Center for GIS, RCHSS, Academia Sinica`_.
The package source code is licensed under the GNU General Public License;
either version 2 of the License, or (at your option) any later version.

.. _CRGIS (Culture Resources Geographic Information System): http://crgis.rchss.sinica.edu.tw/about
.. _Center for GIS, RCHSS, Academia Sinica: http://gis.rchss.sinica.edu.tw/

