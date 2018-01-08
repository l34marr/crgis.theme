# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
import json
from BeautifulSoup import BeautifulSoup as bs
import logging

logger = logging.getLogger('crgis.theme')
LIMIT=20

areaNames = '''[
"北京", "上海", "天津", "重慶", "江蘇", "浙江", "福建省", "廣東", "湖南", "河南省", "湖北省", "江西", "安徽省", "河北省", "山西省", "陝西省", "雲南省", "貴州省", "四川省", "甘肅省", "青海省", "黑龍江省", "吉林省", "遼寧省", "山東省", "海南省", "廣西壯族自治區", "西藏自治區", "內蒙古自治區", "寧夏回族自治區", "新疆維吾爾自治區", "香港特別行政區", "澳門特別行政區", "臺灣"
]'''
ctgrNames = '''[
"寺", "庵", "廟", "殿", "堂", "洞", "俄康", "協會", "活動點", "不詳", "其他"
]'''


class BuddhistQuery(BrowserView):

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        catalog = context.portal_catalog

        area = request.form.get('area[]')
        bgis_type = request.form.get('bgis_type[]')

        query = {'portal_type': 'Buddhist', 'sort_on': 'getId'}

        if (not area) and (not bgis_type):
            return None

        if area:
            query['area1'] = area

        if bgis_type:
            query['bgis_type'] = bgis_type

        brains = catalog(query)
        result = []

#       if len(brains) > 1500:
#           brains = brains[::10]  # unhashable type

        for brain in brains:
            item = brain.getObject()
            bgis_type = ''
            if item.getText():
                try:
                    bgis_type += bs(item.getText()).find('p', {'class': 'ct'}).text.split(': ')[1]
                except:
                    bgis_type += '其他'

            if brain.zgeo_geometry.get('coordinates', None):
                lat = float(brain.zgeo_geometry.get('coordinates')[1])
                lng = float(brain.zgeo_geometry.get('coordinates')[0])
                latlng = [lat, lng]
            else:
                latlng = [0, 0]

            result.append({'latlng': latlng, 'title': brain.Title, 'url': brain.getURL(), 'area': brain.Description, 'bgis_type': bgis_type})
        return json.dumps(result)


class FilterMap(BrowserView):

    template = ViewPageTemplateFile("bdst_filter.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()
        self.areaNames = json.loads(areaNames)
        self.ctgrNames = json.loads(ctgrNames)
        return self.template()

