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

from DateTime.DateTime import *

CNADestaqueSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        'jornal',
        storage=atapi.AnnotationStorage(),
        widget=atapi.LinesWidget(
            label=_(u"Jornal"),
        ),
        required=True,
        vocabulary="getVocabularyJornais"
    ),


    atapi.DateTimeField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            starting_year='2017',
            show_hm=False,
        ),
        validators=('isValidDate'),
        required=True,
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
    """Description of the Example Type"""
    implements(ICNADestaque)

    meta_type = "CNADestaque"
    schema = CNADestaqueSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    jornal = atapi.ATFieldProperty('jornal')

    data = atapi.ATFieldProperty('data')

    texto = atapi.ATFieldProperty('texto')


    def getDefaultTime(self):
        return DateTime()

    def getVocabularyJornais(self):
            return ['Folha de S. Paulo', 'O Estado de S. Paulo', 'O Globo', 'Valor Econômico' ]

    def getDados(self):
        jornal = self.getJornal()
        aux = '  name: "clipping_CNA",\n'
        aux = aux + '  tempo: 7,\n'
        aux = aux + '  jornal: "%s",\n' % jornal[0]
        aux = aux + '  mensagemTitulo: "%s",\n' % self.Title()
        aux = aux + '  mensagemSubtitulo: "%s",\n' % self.getTexto().replace('\r\n','\\n')
        aux = aux + '  data: "%s",\n' % self.getData().strftime('%d/%m/%Y')
        aux = aux + '  logoJornal: "%s.png"\n' % jornal[0]
        return aux


atapi.registerType(CNADestaque, PROJECTNAME)
