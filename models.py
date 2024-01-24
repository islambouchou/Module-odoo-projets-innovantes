# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Projet(models.Model):
    _name = 'innavante.projet'
    _description = "Les Projet"
    nom = fields.Char(string="Nom_Projet", required=True)
    description = fields.Binary(string="Description_projet", required=True)
    date_debut = fields.Date()
 

class  Etudiant(models.Model):
    _name = 'innavante.etudiant'
    _description = "Les étudiants"

    nom = fields.Char(string="Nom_etudiant", required=True)
    matricule = fields.Char(string="Matricule_donateur", required=True)
    projet_id = fields.Many2one("innavante.projet", 
        ondelete="cascade", string="projet", required = True)
 

class Evaluation(models.Model):
    _name = 'innavante.evaluation'
    _description = "Les evaluations"
    nom = fields.Char(string="evaluation", required=True)
    appreciation = fields.Selection ([
                        ('A', 'A'),
                        ('B', 'B'),
                        ('C', 'C'),
                        ('D', 'D'),], string="appréciation")
    recommendation = fields.Char(string = "recommendation")
    project_id = fields.Many2one("innavante.projet", 
        ondelete="cascade", string="projet", required = True)

    evaluateurs_ids = fields.Many2many (
        "innavante.evaluateur", string="Evaluateurs")
    

class Evaluateur(models.Model):
    _name = 'innavante.evaluateur'
    _description = "Les evaluateurs"
    nom = fields.Char(string="Nom_Evaluateur", required=True)
    prenom = fields.Char(string="Prenom_Evaluateur", required=True)
    entreprise_affiliee = fields.Char(string = "Entreprise_affiliee")
    #true
    evaluations_ids = fields.Many2many (
        "innavante.evaluation", string="Evaluations")
    




   