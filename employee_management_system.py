'''
    This module implements a simple employee management system with the following features:
    1. Employee class with attributes: employee_id, name, email, and annual leave days.
    2. LeaveRequest class to handle leave requests with attributes: request_id, employee_id, leave_date, and status.
    3. Methods to book leave, approve/reject leave requests, and check leave balance.
    4. Example usage of the classes to demonstrate functionality.
'''

from datetime import date
from typing import List


class Employee:
    def __init__(self, employee_id: str, name: str, email: str, annual_leave_days: int = 25):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.annual_leave_days = annual_leave_days
        self.leave_requests: List['LeaveRequest'] = []

    def book_leave(self, leave_date: date) -> bool:
        if self.annual_leave_days > 0:
            self.leave_requests.append(
                LeaveRequest(self.employee_id, leave_date))
            self.annual_leave_days -= 1
            return True
        return False

    def get_leave_balance(self) -> int:
        return self.annual_leave_days


class LeaveRequest:
    def __init__(self, employee_id: str, leave_date: date):
        self.request_id = f"req_{employee_id}_{leave_date.isoformat()}"
        self.employee_id = employee_id
        self.leave_date = leave_date
        self.status = "Pending"

    def approve(self):
        self.status = "Approved"

    def reject(self):
        self.status = "Rejected"


# Example Usage
if __name__ == "__main__":
    emp = Employee("EMP001", "Imraan", "imraanm@example.com")
    print(f"Initial leave balance: {emp.get_leave_balance()}")
    
    emp.book_leave(date(2025, 9, 10))
    print(f"Leave balance after booking: {emp.get_leave_balance()}")

    for request in emp.leave_requests:
        print(f"Leave Request ID: {request.request_id}, Status: {request.status}")
        request.approve()
        print(f"Leave Request ID: {request.request_id}, Status after approval: {request.status}")
        request.reject()
        print(f"Leave Request ID: {request.request_id}, Status after rejection: {request.status}")

