__author__ = 'enzyme'
__date__ = '2019/7/11 6:47 PM'
from rest_framework.renderers import JSONRenderer as DRF_JSONRenderer


class JSONRender(DRF_JSONRenderer):
    charset = 'utf-8'
