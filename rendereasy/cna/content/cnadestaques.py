# -*- coding: utf-8 -*-
"""Definition of the CNA Destaques content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cna import cnaMessageFactory as _

from rendereasy.cna.interfaces import ICNADestaques
from rendereasy.cna.config import PROJECTNAME

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

CNADestaquesSchema = folder.ATFolderSchema.copy() + atapi.Schema((

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

CNADestaquesSchema['title'].storage = atapi.AnnotationStorage()
CNADestaquesSchema['description'].storage = atapi.AnnotationStorage()
CNADestaquesSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}
CNADestaquesSchema['downloadlink'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    CNADestaquesSchema,
    folderish=True,
    moveDiscussion=False
)


class CNADestaques(folder.ATFolder):
    """ """
    implements(ICNADestaques)

    meta_type = "CNADestaques"
    schema = CNADestaquesSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    downloadlink = atapi.ATFieldProperty('downloadlink')

    def getDestaques(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/')
        destaques = pc.searchResults(meta_type='CNADestaque',path=path)
        return destaques

    def getDados(self):
        destaques = self.listFolderContents()
        aux = 'var novoProjeto = "' + self.meta_type + '_' + DateTime().strftime("%Y%m%d%H%M%S") + '";\n'

        telas = '['
        cont = 0
        for destaque in destaques:
            cont = cont + 1
            aux = aux + 'var Tela%02d = {\n' % cont
            aux = aux + destaque.getDados()
            aux = aux + '};\n'
            telas = telas + 'Tela%02d, ' % cont
        telas = telas[:-2] + '];\n'

        aux = aux + 'var ext_Telas = ' + telas
        aux = aux + 'var arquivos = [];'

        return aux


atapi.registerType(CNADestaques, PROJECTNAME)
