from flask_restx import Namespace, Resource, fields
from flask import Flask, request, jsonify
from ..utils.db import db
from ..models.customer import Customer

# Create a namespace for customers
customer_ns = Namespace("customers")

# Define a model for the customer data
customer_model = customer_ns.model("customer", {
    "id": fields.Integer(required=True),
    "name": fields.String(required=True),
    "email": fields.String(required=True),
    "mobile": fields.String(required=True)
})

# Route for retrieving all customers
@customer_ns.route('/get_all_customer')
class Display_Customer(Resource):
    @customer_ns.marshal_list_with(customer_model)  # Marshal the response as a list of customers
    @customer_ns.doc(description="Retrieve all the customers from the database")  # Document the route
    def get(self):
        try:
            # Retrieve all customers from the database
            customers = Customer.query.all()
            return customers
        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}, 500
 
# Route for creating a new customer
@customer_ns.route('/create_new_customer')
class CreateCustomer(Resource):
    @customer_ns.expect(customer_model)
    @customer_ns.marshal_with(customer_model)
    @customer_ns.doc(description="Create new customers in the database")
    def post(self):
        try:
            # Extract data from the request payload
            data = customer_ns.payload
            # Create a new customer object
            new_customer = Customer(id=data['id'], name=data['name'], email=data['email'], mobile=data['mobile'])
            # Save the new customer to the database
            new_customer.save()
            return new_customer
        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}, 500
 
# Route for retrieving a customer by ID
@customer_ns.route('/get_customer_by_id<int:id>')
class GetCustomer(Resource):
    @customer_ns.marshal_list_with(customer_model)
    @customer_ns.doc(description="Retrieve details of customers by id from the database",
                     params={"customer_id": "An ID for a given customer"})
    def get(self, id):
        try:
            # Retrieve the customer by ID from the database
            customer = Customer.query.get(id)
            return customer
        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}, 500
 
# Route for updating an existing customer
@customer_ns.route('/update_existing_customer<int:id>')
class UpdateCustomer(Resource):
    @customer_ns.expect(customer_model)
    @customer_ns.marshal_with(customer_model)
    @customer_ns.doc(description="Update details of customer by id from the database",
                     params={"customer_id": "An ID for a given customer"})
    def put(self, id):
        try:
            # Extract data from the request payload
            data = customer_ns.payload
            # Retrieve the existing customer by ID from the database
            existing_customer = Customer.query.get(id)
            # If customer not found, return 404 response
            if not existing_customer:
                return {"message": "Customer not found"}, 404
            # Update customer details with new data
            existing_customer.name = data.get('name', existing_customer.name)
            existing_customer.email = data.get('email', existing_customer.email)
            existing_customer.mobile = data.get('mobile', existing_customer.mobile)
            # Commit changes to the database
            db.session.commit()
            return existing_customer
        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}, 500
 
# Route for deleting a customer
@customer_ns.route('/delete_customer<int:id>')
class DeleteCustomer(Resource):
    @customer_ns.doc(description="Delete details of customer by id from the database",
                     params={"customer_id": "An ID for a given customer"})
    def delete(self, id):
        try:
            # Retrieve the existing customer by ID from the database
            existing_customer = Customer.query.get(id)
            # If customer not found, return 404 response
            if not existing_customer:
                return {"message": "Customer not found"}, 404
            # Delete the customer from the database
            existing_customer.delete()
            return {"message": "Customer Deleted Successfully"}, 204
        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}, 500