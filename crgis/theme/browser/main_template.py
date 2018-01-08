from zope.interface import implements

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from crgis.theme.interfaces import IWgyeTemplate


class WgyeTemplate(BrowserView):
    implements(IWgyeTemplate)

    wgye_template = ViewPageTemplateFile('wgye_template.pt')

    def __call__(self):
        return self.template()

    @property
    def template(self):
        return self.wgye_template

    @property
    def macros(self):
        return self.template.macros

class BdstTemplate(BrowserView):
    implements(IWgyeTemplate)

    bdst_template = ViewPageTemplateFile('bdst_template.pt')

    def __call__(self):
        return self.template()

    @property
    def template(self):
        return self.bdst_template

    @property
    def macros(self):
        return self.template.macros

