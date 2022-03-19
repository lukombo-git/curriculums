from flask import Blueprint, jsonify, request
from models import db, Curriculums
from models import *

curriculum_blueprint=Blueprint('curriculums_api_routes',__name__,url_prefix='/api/curriculums')


#createing a new curriculum
@curriculum_blueprint.route('/create', methods=['GET','POST'])
def create_curriculums():
    try:
        curriculum = Curriculums()
        curriculum.id_candidato = request.form["id_candidato"]
        curriculum.curriculum = request.form["curriculum"]
        curriculum.habilidades  = request.form["habilidades"]
        curriculum.vaga_pontuacao = request.form["vaga_pontuacao"]
        db.session.commit()
        db.session.add(curriculum)
        db.session.commit()
        response ={'message':'Curriculum Criado com sucesso!','result':curriculum.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message':'Erro ao criar o curriculum'}
    return jsonify(response)

#updating a curriculum
@curriculum_blueprint.route('/update_curriculum_id/<id_curriculum>', methods=['GET','POST','PUT'])
def update_curriculum(id_curriculum):
    curriculum = curriculum.query.get(id_curriculum)
    try:
        curriculum.id_candidato = request.form["id_candidato"]
        curriculum.curriculum = request.form["curriculum"]
        curriculum.habilidades  = request.form["habilidades"]
        curriculum.vaga_pontuacao = request.form["vaga_pontuacao"] 
        db.session.commit()
        db.session.add(curriculum)       
    except Exception as e:
        print(str(e))
        response = {'message':'Erro ao criar o candidato','result':curriculum.id_curriculum} 
    return jsonify(response)
   

#deleting a curriculum
@curriculum_blueprint.route('/delete/<id_curriculum>', methods=['DELETE'])
def curriculum_delete(id_curriculum):
    try:
        curriculum = Curriculums.query.get(id_curriculum)
        db.session.delete(curriculum)
        db.session.commit()
        response ={'message':'Curriculum eliminado com sucesso!','result':curriculum.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message':None}
    return jsonify(response)

#getting all curriculums
@curriculum_blueprint.route('/all', methods=['GET'])
def get_all_curriculums():
    all_curriculums = Curriculums.query.all()
    result = [curriculum.serialize() for curriculum in all_curriculums]
    response = {'message':'Returning all curriculums','result': result}
    return jsonify(response)


#counting all curriculums
@curriculum_blueprint.route('/count_curriculums', methods=['GET'])
def count_curriculums():
    total_curriculums = Curriculums.query.count()
    response = {'message':'Returning all curriculums','result': total_curriculums}
    return jsonify(response)

#get a curriculum by id
@curriculum_blueprint.route('/<int:id_curriculum>', methods=['GET'])
def curriculums_id(id_curriculum):
    curriculum = Curriculums.query.filter_by(id_curriculum=id_curriculum).first()
    if curriculum:
        return jsonify({"result":curriculum.serialize()}), 200
    return jsonify({"result":"Curriculum não existe."}), 404

