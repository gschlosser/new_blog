from flask import Flask, Blueprint, render_template, request

auth_blueprint = Blueprint('auth_api', __name__)

@auth_blueprint.route('/')