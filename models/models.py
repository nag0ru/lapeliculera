# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Peliculas(models.Model):
    _name = 'lapeliculera.peliculas'
    _description = 'Modelo para almacenar información sobre películas'
    _inherit = ['mail.thread'] 

    name = fields.Char(string='Título', required=True, help="Introdice un título")
    director = fields.Char(string='Director', required=True)
    industria = fields.Selection([
        ('hollywood', 'Hollywood'),
        ('europea', 'Europea'),
        ('bollywood', 'Bollywood'),
        ('otras', 'Otras')
    ], string='Industria')
    color = fields.Selection([('color','Color'), ('blanco_negro', 'Blanco y Negro')], string ="Tipo de color de la película", default='color')
    duracion = fields.Integer(string='Duración', help='Tiene que se en minutos')
    sinopsis = fields.Text(string='Sinopsis')
    genero_id=fields.Many2one("lapeliculera.genero", required=True)
    x_sequence=fields.Integer(string='Ordenación')

    # Campos de mensajeria
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string='Seguidores', domain=lambda self: [('res_model', '=', 'tu_modulo.producto')], readonly=True)
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Actividades', domain=lambda self: [('res_model', '=', 'tu_modulo.producto')], readonly=True)
    message_ids  = fields.One2many('mail.activity', 'res_id', string='Mensajes', domain=lambda self: [('model', '=', 'tu_modulo.producto')], readonly=True)

 
class Genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Modelo para almacenar información sobre géneros cinematográficos'
    _inherit = ['mail.thread'] 

    name = fields.Selection([
        ('Acción', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Musical', 'Musical'),
        ('Drama', 'Drama'),
        ('Aventura', 'Aventura'),
        ('Western', 'Western'),
        ('Terror', 'Terror'),
        ('Suspense', 'Suspense'),
    ], string='Género', help="Introduzca un Género")
    peliculas_ids=fields.One2many("lapeliculera.peliculas", "genero_id")
    x_sequence=fields.Integer(string='Ordenación')

    # Campos de mensajeria
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string='Seguidores', domain=lambda self: [('res_model', '=', 'tu_modulo.producto')], readonly=True)
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Actividades', domain=lambda self: [('res_model', '=', 'tu_modulo.producto')], readonly=True)
    message_ids  = fields.One2many('mail.activity', 'res_id', string='Mensajes', domain=lambda self: [('model', '=', 'tu_modulo.producto')], readonly=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result
    #name[values]
