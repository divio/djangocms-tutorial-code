#-*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import PollsMenu


class PollsApp(CMSApp):
    name = _("Poll App")  # give your app a name, this is required
    urls = ["polls.urls"]  # link your app to url configuration(s)
    app_name = "polls"
    menus = [PollsMenu]

apphook_pool.register(PollsApp)  # register your app
