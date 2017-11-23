from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cna import cnaMessageFactory as _



class IVinheta(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    downloadlink = schema.TextLine(
        title=_(u"Download Link"),
        required=False,
        description=_(u"Field description"),
    )
#
    video = schema.Bytes(
        title=_(u"Video"),
        required=True,
        description=_(u"Field description"),
    )
#
