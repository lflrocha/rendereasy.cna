# -*- coding: utf-8 -*-
"""Definition of the Card content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cna import cnaMessageFactory as _

from rendereasy.cna.interfaces import ICard
from rendereasy.cna.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

CardSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'subtitulo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Subtítulo"),
        ),
    ),

    atapi.DateTimeField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
        ),
        required=True,
        validators=('isValidDate'),
    ),

    atapi.FileField(
        'foto',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Foto"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),

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

CardSchema['title'].storage = atapi.AnnotationStorage()
CardSchema['description'].storage = atapi.AnnotationStorage()
CardSchema['downloadlink'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
CardSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(CardSchema, moveDiscussion=False)


class Card(base.ATCTContent):
    """ """
    implements(ICard)

    meta_type = "Card"
    schema = CardSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    data = atapi.ATFieldProperty('data')
    foto = atapi.ATFieldProperty('foto')
    subtitulo = atapi.ATFieldProperty('subtitulo')
    downloadlink = atapi.ATFieldProperty('downloadlink')



    def getDados(self):
        titulo = self.Title()
        subtitulo = self.getSubtitulo()
        foto = self.getFilename('foto')
        data = self.getData()
        endereco = self.absolute_url()


        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + '{\n'
        aux = aux + 'name: "card",\n'
        aux = aux + 'modelo: 1,\n'
        aux = aux + 'titulo: "%s",\n' % titulo
        aux = aux + 'subtitulo: "%s",\n' % subtitulo
        aux = aux + 'foto: "%s",\n' % foto
        aux = aux + 'data: "%s",\n' % data.strftime('%d-%b')
        aux = aux + '}, \n'
        aux = aux + ']\n'
        aux = aux + 'var arquivos = ['
        aux = aux + '("%s/at_download/foto/", "%s"), ' % (endereco, foto)
        aux = aux + '];'
        return aux

atapi.registerType(Card, PROJECTNAME)
