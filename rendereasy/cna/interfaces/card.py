from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cna import cnaMessageFactory as _



class ICard(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    downloadlink = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
#
