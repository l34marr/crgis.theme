Installation
------------

To install crgis.theme using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, here is the easiest way:

* Check out the code from GitHub:

    $ cd zinstance/src
    $ git clone https://github.com/l34marr/crgis.theme.git

* Add ``crgis.theme`` to the develop.cfg file:

    [sources]
    ...
    crgis.theme = fs crgis.theme

    [buildout]
    ...
    eggs +=
        ...
        crgis.theme
       
* Re-run buildout, e.g. with:

    $ ./bin/buildout -c develop.cfg

* Start the instance:

    $ ./bin/plonectl fg

* Go *Site Setup* *Add-ons* to activate the package:

