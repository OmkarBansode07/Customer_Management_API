from api.models.customer import Customer  # Importing the Customer model from api.models.customer module
import pytest  # Importing pytest for testing
 


class TestCustomerAPI:
    # Test case to retrieve all customers
    @pytest.mark.get  # Marking the test as a GET request test
    def test_get_all_customers(self,client):
        # Retrieving all customers from the database
        all_customers= Customer.query.all()
        print(all_customers)  # Printing the retrieved customers (for debugging)
        if len(all_customers) != 0:
                response = client.get('/customers/get_all_customer')  # Sending a GET request to retrieve all customers
                assert response.status_code == 200  # Asserting that the response status code is 200 (OK)
        else:
            # Handling any exceptions that may occur during the test
            with pytest.raises(Exception) as e:    
                print("Database has no customer data!!")
                pytest.fail(f"Exception occurred:{str(e)}")  # Returning a message if exception occurred


    # Test case to create a new customer in the database
    @pytest.mark.post    # Marking the test as a POST request test
    def test_customer_is_created_in_the_database(self,client):
        data = {  # Data for creating a new customer
            "id":5,
            "name": "Customer",
            "email": "test@example.com",
            "mobile": "1234567890"
        }
        customer_data = Customer.query.filter_by(id=data['id']).first()
        if customer_data is None : 
                response = client.post('/customers/create_new_customer', json=data)  # Sending a POST request to create a new customer
                assert response.status_code == 200  # Asserting that the response status code is 200 (OK)
        else:
            with pytest.raises(Exception) as e:    
                print("Data is already present in database")
                # Handling any exceptions that may occur during the test
                pytest.fail(f"Exception occurred:{str(e)}")  # Returning a message if exception occurred


    # Test case to retrieve customer details by ID
    @pytest.mark.get  # Marking the test as a GET request test
    @pytest.mark.parametrize("customer_id",[1,2,3])   # Parametrizing the test with customer ID
    def test_get_customer_details_by_id(self,client,customer_id):
        existing_customer = Customer.query.filter_by(id = customer_id).first()
        if existing_customer is not None:
            response = client.get(f'/customers/get_customer_by_id{customer_id}')  # Sending a GET request to retrieve customer details by ID
            assert response.status_code == 200  # Asserting that the response status code is 200 (OK)
        else:
            with pytest.raises(Exception) as e:    
                print("Customer data is not present in database")
                pytest.fail(f"Exception occurred:{str(e)}")  # Returning a message if exception occurred

    
    # Test case to update an existing customer
    @pytest.mark.put  # Marking the test as a PUT request test
    def test_update_existing_customer(self,client):
        data = {  # Data for updating an existing customer
            "name": "omkar",
            "email": "omkarbansode@gmail.com",
            "mobile": "8329457877"
        }
        customer_id = 3
        existing_customer = Customer.query.filter_by(id=customer_id).first()  # Querying the database to find an existing customer
        if existing_customer is not None:
            response = client.put(f'/customers/update_existing_customer{existing_customer.id}', json=data)  # Sending a PUT request to update an existing customer
            assert response.status_code == 200  # Asserting that the response status code is 200 (OK)
        else:
            with pytest.raises(Exception) as e:
                print("Customer data is not present in database")
                pytest.fail(f"Exception occurred:{str(e)}")  # Returning a message if exception occurred

        updated_customer = Customer.query.get(existing_customer.id)  # Retrieving the updated customer from the database
        assert updated_customer is not None  # Asserting that the updated customer exists in the database
    
    # Test case to delete a customer
    @pytest.mark.delete     # Marking the test as a DELETE request test
    @pytest.mark.parametrize("customer_id",[1])  # Parametrizing the test with customer ID
    def test_delete_customer(self,client,customer_id):
        existing_customer = Customer.query.filter_by(id=customer_id).first()
        if existing_customer is not None:
            response = client.delete(f'/customers/delete_customer{customer_id}')  # Sending a DELETE request to delete a customer
            assert response.status_code == 204  # Asserting that the response status code is 204 (No Content)
        else:
            with pytest.raises(Exception) as e:
                print("Customer data is not present in database")
                pytest.fail(f"Exception occurred:{str(e)}") # Failing the test with an exception message if an error occurs
        
        deleted_customer = Customer.query.get(customer_id)  # Querying the database to find the deleted customer
        assert deleted_customer is None  # Asserting that the deleted customer does not exist in the database







