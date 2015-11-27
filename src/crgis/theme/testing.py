# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import crgis.theme


class CrgisThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=crgis.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'crgis.theme:default')


CRGIS_THEME_FIXTURE = CrgisThemeLayer()


CRGIS_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CRGIS_THEME_FIXTURE,),
    name='CrgisThemeLayer:IntegrationTesting'
)


CRGIS_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CRGIS_THEME_FIXTURE,),
    name='CrgisThemeLayer:FunctionalTesting'
)


CRGIS_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CRGIS_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CrgisThemeLayer:AcceptanceTesting'
)
