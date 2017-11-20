from zope.interface import Interface


class ICustomTheme(Interface):
    """Marker Interface that Defines a Zope 3 Browser Layer.
    """

class IFrontPage(Interface):
    """Browser View for FrontPage Logic
    """

class IAboutView(Interface):
    """Browser View for About Logic
    """

class IWgyeTemplate(Interface):
    """Interface to the view that generated the wgye_template
    """
