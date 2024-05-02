from odoo import api,fields, models

class trainer_trainer(models.Model):
    _name = "trainer.trainer"
    _description = "Trainer registration."


    name=fields.Char()

    age=fields.Char()    
