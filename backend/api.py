from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session


from class_object.Calculator import Calculator
from db.engine import create_tables, get_session
from db.models import ResultModel
from tools.csv import read_csv_file


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start_db():
    create_tables()


class calculatarInputSchema(BaseModel):
    expression: str

    @field_validator("expression")
    @classmethod
    def isString(cls, value):
        if not isinstance(value, str):
            raise ValueError("expression must be a string")
        return value


@app.post("/calculator")
def calculator(request: calculatarInputSchema, session: Session = Depends(get_session)):
    try:
        print("hit /calculator endpoint", request.expression)
        calculator = Calculator()
        result = calculator.get_expression_result(request.expression)

        result_model = ResultModel(expression=request.expression,value=result)
        session.add(result_model)
        session.commit()

        return {"result": result}
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.get("/get_results")
def get_results(session: Session = Depends(get_session)):
    result = session.query(ResultModel).all()
    return {"result": [{"expression": r.expression, "value": r.value} for r in result]}


@app.get("/get_csv_data")
async def get_csv_data():
    file_path = "username.csv"

    try:
        result = read_csv_file(file_path)
        return {"result": result}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
