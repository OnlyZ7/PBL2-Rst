import datetime
from flask import Blueprint, render_template,redirect,url_for,request
from models import BillingForm, Ticket, db , BillingBillingForms , Billing
from sqlalchemy import func

billing = Blueprint("billing", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")

@billing.route("/pagamento")
def payment():
    return render_template("/billing/pagamento.html")


@billing.route("/cadastro-pagamento", methods=["POST","GET"])
def cadastro_pagamento():
    
    name = request.form['name']
    description = request.form['description']
    BillingForms = BillingForm.add_billing_form(name,description)

    return "Dados salvos com sucesso"


@billing.route("/cadastro-comanda", methods=["POST","GET"])
def cadastro_comanda():

    billing_forms = BillingForm.get_billing_forms()
    tickets_forms = db.session.query(Ticket.client_id).distinct().all()
    
    return render_template("/billing/cadastro-comanda.html", billing_forms =billing_forms,tickets_forms=tickets_forms)

@billing.route("/calcular-gastos", methods=["POST","GET"])
def calcular_gastos():

    billing_form_id = request.form['billing_form_id']
    tickets_form_id = request.form['tickets_form_id']

    gastos = db.session.query(db.func.sum(Ticket.purchase_total)).filter_by(client_id=tickets_form_id).first()
    valor_total = gastos[0] if gastos[0] is not None else 0

    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")

    Billing.add_biling(valor_total,date_string)
    id_billing = Billing.get_billing()

    num_id_billing = len(id_billing)

    BillingBillingForms.add_billing_billing(num_id_billing,billing_form_id,valor_total)

    Ticket.ticket_asseg(tickets_form_id,num_id_billing)

    return "Dados salvos"
