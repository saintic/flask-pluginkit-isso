# -*- coding: utf-8 -*-
"""
    isso
    ~~~~

    A Comment System

    :copyright: (c) 2019 by Mr.tao.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

from __future__ import absolute_import
try:
    from config import PLUGINS
except ImportError:
    PLUGINS = {}
__plugin_name__ = "isso"
__description__ = "Isso is a lightweight commenting server similar to Disqus."
__author__ = "Mr.tao <staugur@saintic.com>"
__version__ = "0.1.0"
__url__ = "https://github.com/flask-pluginkit/flask-pluginkit-isso"
__license__ = "BSD 3-Clause"
if PLUGINS.get("ISSO", {}).get("enable") in ("false", "False", False):
    __state__ = "disabled"
else:
    __state__ = "enabled"


def register():
    return dict(
        tep={
            "isso_content": "isso/content.html",
            "isso_script": "isso/script.html"
        }
    )
