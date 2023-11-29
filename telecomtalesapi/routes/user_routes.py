
from telecomtalesapi import app, db
from telecomtalesapi.models.user import User
from flask import request, jsonify

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)  # This hashes the password and stores it
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201
