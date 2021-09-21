# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class OdooAndroidSync(http.Controller):

    @http.route('/attendance/v1/hours/<user_id>/<day_week>', auth='user', methods=['GET'])
    def get_attendance_hours(self, user_id, day_week, **kw):
        try:
            calendar_id = http.request.env['hr.employee'].sudo().search(
                [('user_id', '=', int(user_id))]).resourse_calendar_id.id
            hours = http.request.env['resource.calendar.attendance'].sudo().search_read(
                [('calendar_id', '=', int(calendar_id)), ('day_week', '=',)],
                ['hour_from', 'hour_to'])
            return build_response(hours)
        except Exception as e:
            return build_response({'err': str(e)})

    def build_response(self, entity):
        response = json.dumps(entity, ensure_ascii=False).encode('utf8')
        return Response(response, content_type='application/json;charset=utf-8', status=200)
