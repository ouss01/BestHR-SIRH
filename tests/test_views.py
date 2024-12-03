from rest_framework.test import APITestCase
from rest_framework import status
from EmployeeApp.models import Department, Employee

class DepartmentAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR")

    def test_get_all_departments(self):
        response = self.client.get('/api/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_department(self):
        data = {"name": "Finance"}
        response = self.client.post('/api/departments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_department(self):
        data = {"name": ""}
        response = self.client.post('/api/departments/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_update_department(self):
        data = {"name": "Human Resources"}
        response = self.client.put(f'/api/departments/{self.department.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        response = self.client.delete(f'/api/departments/{self.department.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(name="John Doe", department_id=1)

    def test_get_all_employees(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_employee(self):
        response = self.client.get(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_employee(self):
        data = {"name": "Jane Doe", "department_id": 1}
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_update_employee(self):
        data = {"name": "John Smith", "department_id": 1}
        response = self.client.put(f'/api/employees/{self.employee.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        response = self.client.delete(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
