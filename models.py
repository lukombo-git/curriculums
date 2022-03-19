from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

#Creating the areas model
class Curriculums(db.Model):
    id_curriculum = db.Column(db.Integer, primary_key=True)
    id_candidato = db.Column(db.String(255))
    curriculum = db.Column(db.String(255))
    habilidades = db.Column(db.String(255))
    vaga_pontuacao  = db.Column(db.Integer)
    

    def __repr__(self):
        return f'<Curriculm {self.id_curriculum} {self.id_curriculum}'
    
    def serialize(self):
        return {
            'id_curriculum':self.id_curriculum,
            'id_candidato':self.id_candidato,
            'curriculum':self.curriculum,
            'habilidades':self.habilidades,
            'vaga_pontuacao':self.vaga_pontuacao
        }