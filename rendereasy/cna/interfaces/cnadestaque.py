from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cna import cnaMessageFactory as _



class ICNADestaque(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    veiculo = schema.List(
        title=_(u"Veiculo"),
        required=False,
        description=_(u"Field description"),
    )
#
    data = schema.Date(
        title=_(u"Data"),
        required=True,
        description=_(u"Field description"),
    )
#
    texto = schema.Text(
        title=_(u"Texto"),
        required=False,
        description=_(u"Field description"),
    )
#
