from ..utils.db import db  # Import the database instance
 
# Define the Customer model class
class Customer(db.Model):
    # Define the table name for the model
    __tablename__ = "customers"

    # Define columns for the table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for the customer ID
    name = db.Column(db.String(100), nullable=False)  # Column for the customer's name
    email = db.Column(db.String(100), nullable=False)  # Column for the customer's email
    mobile = db.Column(db.String(10), nullable=False)  # Column for the customer's mobile number

    # Define the string representation of the model
    def __str__(self):
        return f"{self.id}>"  # Return a string representation of the customer object

    # Method to save the customer to the database
    def save(self):
        db.session.add(self)  # Add the customer object to the current session
        db.session.commit()  # Commit the changes to the database

    # Method to delete the customer from the database
    def delete(self):
        db.session.delete(self)  # Delete the customer object from the current session
        db.session.commit()  # Commit the changes to the database