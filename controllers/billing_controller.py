from flask import Blueprint, render_template,redirect,url_for,request

billing = Blueprint("billing", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")

@billing.route("/pagamento")
def payment():
    return render_template("/billing/pagamento.html")

@billing.route("/cadastro-comanda")
def cadastro_comanda():
    return render_template("/billing/cadastro-comanda.html")

@billing.route("/metodo-dinheiro", methods=["POST"])
def salvar_metodo_dinheiro():
    nome = request.form["name-dinheiro"]
    cpf = request.form["cpf-dinheiro"]
    
    return "Dados salvos com sucesso"
