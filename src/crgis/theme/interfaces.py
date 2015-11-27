# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICrgisThemeLayer(IDefaultBrowserLayer):
    """Marker Interface Defining a Browser Layer."""
