## Script (Python) "setWorkflowState"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=acao
##title=
##
from Products.CMFCore.utils import getToolByName

workflowTool = getToolByName(context, 'portal_workflow')

if acao in ['finalizar', 'gerar', 'retornar', 'erro']:
    workflowTool.doActionFor(context, acao)
