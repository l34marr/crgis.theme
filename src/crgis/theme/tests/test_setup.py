# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from crgis.theme.testing import CRGIS_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that crgis.theme is properly installed."""

    layer = CRGIS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if crgis.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'crgis.theme'))

    def test_browserlayer(self):
        """Test that ICrgisThemeLayer is registered."""
        from crgis.theme.interfaces import (
            ICrgisThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ICrgisThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CRGIS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['crgis.theme'])

    def test_product_uninstalled(self):
        """Test if crgis.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'crgis.theme'))

    def test_browserlayer_removed(self):
        """Test that ICrgisThemeLayer is removed."""
        from crgis.theme.interfaces import \
            ICrgisThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICrgisThemeLayer, utils.registered_layers())
