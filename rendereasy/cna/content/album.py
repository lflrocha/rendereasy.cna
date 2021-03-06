# -*- coding: utf-8 -*-
"""Definition of the Album content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cna import cnaMessageFactory as _

from rendereasy.cna.interfaces import IAlbum
from rendereasy.cna.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

AlbumSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'downloadlink',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Download link"),
        ),
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

AlbumSchema['title'].widget.label = _(u"Nome do Álbum")
AlbumSchema['title'].storage = atapi.AnnotationStorage()
AlbumSchema['description'].storage = atapi.AnnotationStorage()
AlbumSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['downloadlink'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    AlbumSchema,
    folderish=True,
    moveDiscussion=False
)


class Album(folder.ATFolder):
    """ """
    implements(IAlbum)

    meta_type = "Album"
    schema = AlbumSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    downloadlink = atapi.ATFieldProperty('downloadlink')

    def getFotos(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/')
        fotos = pc.searchResults(meta_type='Foto',path=path)
        return fotos

    def getDados(self):
        fotos = self.listFolderContents()
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [\n'
        aux = aux + '{\n'
        aux = aux + 'name: "vinheta",\n'
        aux = aux + 'texto: "%s"\n' % self.Title()
        aux = aux + '},\n'
        for foto in fotos:
            arquivo = foto.getFilename('arquivo')
            legenda = foto.getLegenda()
            aux = aux + '{\n'
            aux = aux + 'name: "fotos",\n'
            aux = aux + 'tempo: 10,\n'
            aux = aux + 'legenda: "%s",\n' % legenda
            aux = aux + 'foto: "%s",\n' % arquivo
            aux = aux + 'bg: "blur"\n'
            aux = aux + '}, \n'

        aux = aux + '{\n'
        aux = aux + 'name: "assinatura",\n'
        aux = aux + 'texto: "www.cnabrasil.org.br"\n'
        aux = aux + '}\n'
        aux = aux + ']\n'

        aux = aux + 'var arquivos = ['
        for foto in fotos:
            filename = foto.getFilename('arquivo')
            endereco = self.absolute_url() + '/' + foto.getId()
            aux = aux + '("%s/at_download/arquivo/", "%s"), ' % (endereco, filename)

        aux = aux[:-2] + '];'
        return aux

atapi.registerType(Album, PROJECTNAME)
