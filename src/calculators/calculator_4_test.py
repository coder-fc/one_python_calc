from pytest import raises
from typing import Dict, List
from .calculator_4 import Calculator4


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [5, 15, 255, 8]})
    calculator_4 = Calculator4()

    response = calculator_4.calculate(mock_request)

    assert response == {
        'data': {
            'Calculator': 4, 'average': 70.75
        }
    }
