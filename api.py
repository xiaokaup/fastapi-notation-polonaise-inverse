from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from fastapi import FastAPI, HTTPException

from tools.Calculator import Calculator

app = FastAPI()


class calculatarInputSchema(BaseModel):
    expression: str

    @field_validator("expression")
    @classmethod
    def isString(cls, value):
        if not isinstance(value, str):
            raise ValueError("expression must be a string")
        return value


@app.post("/calculator")
def calculator(request: calculatarInputSchema):
    try:
        calculator = Calculator()
        result = calculator.get_expression_result(request.expression)
        return {"result": result}
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
