from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cna import cnaMessageFactory as _



class ICard(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    data = schema.Date(
        title=_(u"Data"),
        required=True,
        description=_(u"Field description"),
    )
#
    foto = schema.Bytes(
        title=_(u"Foto"),
        required=True,
        description=_(u"Field description"),
    )
#
    subtitulo = schema.TextLine(
        title=_(u"Subtitulo"),
        required=False,
        description=_(u"Field description"),
    )
#
    downloadlink = schema.TextLine(
        title=_(u"Download link"),
        required=False,
        description=_(u"Field description"),
    )
#
