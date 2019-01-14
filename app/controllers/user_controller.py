from flask import Blueprint,request

bp = Blueprint('user', __name__, url_prefix='/rewards')

@bp.route('/v1/users/', methods=('GET', 'POST'))
def register():
	if request.method == 'GET':
		return "push"
