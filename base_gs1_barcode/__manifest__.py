# -*- coding: utf-8 -*-
##############################################################################
#
#    This module is copyright (C) 2012-2014 Numérigraphe SARL.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'GS1 Barcode API',
    'summary': 'Decoding API for GS1-128 (aka UCC/EAN-128) and GS1-Datamatrix',
    'version': '12.0.1.0.0',
    'author': 'Numérigraphe,Odoo Community Association (OCA),Media Engagers',
    'website': 'http://numerigraphe.com',
    'category': 'Generic Modules/Inventory Control',
    'depends': [
        'product',
    ],
    'data': [
        'views/gs1_barcode.xml',
        'views/res_users.xml',
        'data/gs1_barcode.csv',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'AGPL-3',
}