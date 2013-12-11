# -*- coding: utf-8 -*-
##############################################################################
#
#    yeahliu
#    Copyright (C) yeahliu (<talent_qiao@163.com>).
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

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import netsvc



class wkf_logs(osv.osv):
    _inherit = "workflow.logs"
    
    def _get_employee(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for log in self.browse(cr,uid,ids,context=context):
            if log.uid.employee_ids:
                res[log.id] = log.uid.employee_ids[0].id
        return res 
    
    def _get_job(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for log in self.browse(cr,uid,ids,context=context):
            if log.uid.employee_ids and len(log.uid.employee_ids)>=1 :
                res[log.id] = log.uid.employee_ids[0].job_id.id
        return res
           

    _columns = {
        'employee_id': fields.function(_get_employee, string='人员', type='many2one', 
                                relation="hr.employee"),
        'job_id':fields.function(_get_job, string='职位', type='many2one', 
                                relation="hr.job"),      
    }

wkf_logs()

        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

