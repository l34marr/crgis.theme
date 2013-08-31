from plone.app.layout.viewlets.common import LogoViewlet

class LogoViewlet(LogoViewlet):
    def update(self):
        super(LogoViewlet, self).update()
        self.logo_tag = '<img src="' + self.navigation_root_url + '/++resource++crgis.theme/logo.png" alt="CRGIS Logo">'

