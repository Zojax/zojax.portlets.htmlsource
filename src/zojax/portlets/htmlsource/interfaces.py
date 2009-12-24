##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, schema
from zope.i18n import MessageFactory
from zojax.richtext.field import RichText

_ = MessageFactory('zojax.portlets')


class IHTMLSourcePortlet(interface.Interface):
    """Portlet based on HTML source """

    label = schema.TextLine(
        title = _(u'Label'),
        default = u'',
        required = False)

    decoration = schema.Bool(
        title = _(u'Portlet decoration'),
        description = _(u'Show portlet decoration, or just html.'),
        default = True,
        required = False)

    cssClass = schema.TextLine(
        title = _(u'CSS class'),
        required = False)

    source = RichText(
        title = _(u'Source'),
        description = _(u'Entire HTML source.'),
        default = u'',
        required = True)
