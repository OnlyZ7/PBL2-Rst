from models.db import db
from models import Client
from models import Billing

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer(), primary_key=True)
    client_id = db.Column(db.Integer(), db.ForeignKey(Client.id, ondelete='CASCADE'))
    billing_id = db.Column(db.Integer(), db.ForeignKey(Billing.id), nullable=True)
    creation_datetime = db.Column(db.DateTime, nullable = False)
    purchase_total = db.Column(db.Float, nullable=True)
    items = db.Column(db.Integer, nullable = False, default = '0')

    orders = db.relationship('Order', backref='tickets')

    def save_tickets(billing_id):
        billing_form = Ticket(billing_id=billing_id)
        db.session.add(billing_form)
        db.session.commit()

    def get_tickets():
        return Ticket.query.all()
    
    
    def ticket_asseg(client_id, billing_id):
        # Filtrar todos os tickets com o mesmo client_id
        tickets = Ticket.query.filter_by(client_id=client_id).all()

        # Atualizar o billing_id de cada ticket
        for ticket in tickets:
            ticket.billing_id = billing_id

        # Salvar as alterações no banco de dados
        db.session.commit()