from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class ICustomTheme(IDefaultPloneLayer):
    """Marker Interface that Defines a Zope 3 Browser Layer.
    """

class IFrontPage(Interface):
    """Browser View for FrontPage Logic
    """

class IAboutView(Interface):
    """Browser View for About Logic
    """

