from rest_framework.test import APITestCase
from rest_framework import status
from EmployeeApp.models import Employee

class EmployeeAPITests(APITestCase):

    def setUp(self):
        # Create an employee for testing purposes
        self.employee_url = '/api/employees/'  # Assuming the URL pattern for employees.
        self.employee = Employee.objects.create(name="John Doe")

    def test_get_all_employees(self):
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_employee(self):
        response = self.client.get(f'{self.employee_url}{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_employee(self):
        data = {"name": "Jane Doe"}
        response = self.client.post(self.employee_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_employee(self):
        # Invalid because "name" field is missing
        data = {}
        response = self.client.post(self.employee_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_update_employee(self):
        update_url = f'{self.employee_url}{self.employee.id}/'
        data = {"name": "John Smith"}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        delete_url = f'{self.employee_url}{self.employee.id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
