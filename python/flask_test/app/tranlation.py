# coding=utf-8
from __future__ import absolute_import

from flask_babelex import gettext, ngettext


def _(*args, **kwargs):
    return gettext(*args, **kwargs)

# _ = gettext
n_ = ngettext
