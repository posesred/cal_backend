"""
Author Sanatjon Burkhanov
github: posesred
"""
from app.endpoints.routes import add_new_route
from fastapi.testclient import TestClient
from app.api.operations.schemas import GetCalculatorOperation


app = add_new_route()


client = TestClient(app)
def test_query():
    operation_input = GetCalculatorOperation(left_number=5, right_number=6, operation='+')
    response = client.post("/api/operation/get_operation", json=operation_input.dict())
    assert response.json()
    assert response.status_code == 200
