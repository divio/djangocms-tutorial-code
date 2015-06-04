#-*- coding: utf-8 -*-
from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .cms_appconfig import FaqConfig


class FaqApp(CMSConfigApp):
    name = _("Faq App")
    urls = ["faq.urls"]
    app_name = "faq"
    app_config = FaqConfig

apphook_pool.register(FaqApp)
