from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class People(BaseModel):
    name: str
    age: int
    address: str
    salary: float


@app.post('/insert')
def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


# Try http://0.0.0.0:8001/query/123 in browser
@app.get('/query/{uid}')
def query(uid: int):
    msg = f'你查询的 uid 为：{uid}'
    return {'success': True, 'msg': msg}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)