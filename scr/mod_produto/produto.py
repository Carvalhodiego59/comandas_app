from flask import Blueprint, render_template
bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/',methods=['GET', 'POST'])
def formListaProduto():
  return render_template('formListaproduto.html'), 200

@bp_produto.route('/form-produto/', methods=['GET'])
def formProduto():
  return render_template('formProduto.html')