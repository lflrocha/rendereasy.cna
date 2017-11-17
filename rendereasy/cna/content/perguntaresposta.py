# -*- coding: utf-8 -*-
"""Definition of the Pergunta Resposta content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cna import cnaMessageFactory as _

from rendereasy.cna.interfaces import IPerguntaResposta
from rendereasy.cna.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

PerguntaRespostaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'downloadlink',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Download link"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PerguntaRespostaSchema['title'].storage = atapi.AnnotationStorage()
PerguntaRespostaSchema['description'].storage = atapi.AnnotationStorage()
PerguntaRespostaSchema['downloadlink'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(PerguntaRespostaSchema, moveDiscussion=False)


class PerguntaResposta(base.ATCTContent):
    """ """
    implements(IPerguntaResposta)

    meta_type = "PerguntaResposta"
    schema = PerguntaRespostaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    downloadlink = atapi.ATFieldProperty('downloadlink')


atapi.registerType(PerguntaResposta, PROJECTNAME)
