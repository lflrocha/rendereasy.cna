# -*- coding: utf-8 -*-
"""Definition of the CNA Destaque content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cna import cnaMessageFactory as _

from rendereasy.cna.interfaces import ICNADestaque
from rendereasy.cna.config import PROJECTNAME

from Products.ATVocabularyManager import NamedVocabulary
from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

CNADestaqueSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'veiculo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Veículo"),
        ),
        vocabulary=NamedVocabulary("veiculos"),
        required=True,
    ),

    atapi.DateTimeField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            starting_year='2017',
            show_hm=False,
        ),
        required=True,
        validators=('isValidDate'),
        default_method = 'getDefaultTime',
    ),

    atapi.TextField(
        'texto',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Texto"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CNADestaqueSchema['title'].storage = atapi.AnnotationStorage()
CNADestaqueSchema['description'].storage = atapi.AnnotationStorage()
CNADestaqueSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaqueSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(CNADestaqueSchema, moveDiscussion=False)


class CNADestaque(base.ATCTContent):
    """ """
    implements(ICNADestaque)

    meta_type = "CNADestaque"
    schema = CNADestaqueSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    veiculo = atapi.ATFieldProperty('veiculo')
    data = atapi.ATFieldProperty('data')
    texto = atapi.ATFieldProperty('texto')

    def getDefaultTime(self):
        return DateTime()


atapi.registerType(CNADestaque, PROJECTNAME)
