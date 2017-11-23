from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cna import cnaMessageFactory as _



class IInstagram(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    downloadlink = schema.TextLine(
        title=_(u"Download Link"),
        required=False,
        description=_(u"Field description"),
    )
#
