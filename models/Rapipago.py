# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from openerp import api, fields, models 
from datetime import datetime 

class Rapipago(models.Model): 
    _name = 'ej.Rapipago' 
    Codigo_Empresa = fields.Char(string='Codigo_Empresa', required=True) 
 
