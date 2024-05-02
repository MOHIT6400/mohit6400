from odoo import api,fields, models

class measurement_measurement(models.Model):
    _name = "measurement.measurement"
    _description = "GYM MEASUREMENT"

    
    date = fields.Date()
    weight = fields.Float(string='Weight (kg)')
    height = fields.Float(string='Height (cm)')
    bmi = fields.Float(string='BMI')
    bmr = fields.Float(string='BMR')
    neck = fields.Float(string='Neck (cm)')
    chest = fields.Float(string='Chest (cm)')
    biceps = fields.Float(string='Biceps (cm)')
    waist = fields.Float(string='Waist (cm)')
    hips = fields.Float(string='Hips (cm)')
    thighs = fields.Float(string='Thighs (cm)')
    calf = fields.Float(string='Calf (cm)')

    member_id = fields.Many2one('members.members', string='Member')


    