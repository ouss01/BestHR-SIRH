from rest_framework.test import APITestCase
from rest_framework import status
from EmployeeApp.models import Department, Employee

class DepartmentAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.department_url = '/api/departments/'  # Assuming DRF routers or a similar URL pattern.

    def test_get_all_departments(self):
        response = self.client.get(self.department_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_department(self):
        data = {"name": "Finance"}
        response = self.client.post(self.department_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_department(self):
        data = {"name": ""}
        response = self.client.post(self.department_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_update_department(self):
        update_url = f'{self.department_url}{self.department.id}/'
        data = {"name": "Human Resources"}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        delete_url = f'{self.department_url}{self.department.id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(name="John Doe", department=self.department)
        self.employee_url = '/api/employees/'  # Assuming DRF routers or a similar URL pattern.

    def test_get_all_employees(self):
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_employee(self):
        response = self.client.get(f'{self.employee_url}{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_employee(self):
        data = {"name": "Jane Doe", "department": self.department.id}
        response = self.client.post(self.employee_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_employee(self):
        # Invalid because "department" field is missing.
        data = {"name": "Jane Doe"}
        response = self.client.post(self.employee_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_update_employee(self):
        update_url = f'{self.employee_url}{self.employee.id}/'
        data = {"name": "John Smith", "department": self.department.id}
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        delete_url = f'{self.employee_url}{self.employee.id}/'
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
