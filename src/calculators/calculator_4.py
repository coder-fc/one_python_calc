from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict, List


class Calculator4:
    def __init__(self) -> None:
        pass

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__calculate_average(input_data)

        formate_response = self.__format_response(average)

        return formate_response

    def __calculate_average(self, numbers: List) -> Dict:
        average = sum(numbers) / len(numbers)

        return average

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": average
            }
        }
