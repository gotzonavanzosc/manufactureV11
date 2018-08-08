# © Copyright 2018 Gotzon Imaz - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Customer')
#    related='move_prod_id.procurement_id.sale_line_id.order_id.partner_id'
    sale_order_id = fields.Many2one(
        comodel_name='sale.order', string='Sale Order')
#    related='move_prod_id.procurement_id.sale_line_id.order_id'
    sale_line_id = fields.Many2one(
        comodel_name='sale.order.line', string='Sale Line')
#    related='move_prod_id.procurement_id.sale_line_id'

