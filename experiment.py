from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,Optional
from fastapi.responses import JSONResponse
from database import get_db

app=FastAPI()

class Student(BaseModel):
    name:Annotated[str,Field(...,description='Name of student')]
    std:Annotated[int,Field(...,gt=10,lt=13,description='Class of student')]
    contact:Annotated[Optional[str],Field(default=None,description='Contact number')]
    doj:Annotated[Optional[str],Field(default=None,description='Date of joining',examples=['2026-04-08'])]
    status:Annotated[Literal['active','inactive'],Field(default='active',description='active or inactive')]

def load_data():
    con=get_db()
    cur=con.cursor()
    cur.execute('select * from students')
    data=cur.fetchall()
    return data
@app.get('/')
def welcome():
    return 'WELCOME TO CHEMISTRY HUB'

@app.get('/details')
def info():
    data=load_data()
    return data

@app.post('/add_stu')
def add_stu(student: Student):
    con=get_db()
    cur=con.cursor()    
    cur.execute(
        'INSERT INTO students (name, standard,phone,join_date, status) VALUES (%s,%s,%s,%s,%s)',
        (student.name, student.std, student.contact, student.doj, student.status)
    )
    con.commit()
    return JSONResponse(
        status_code=201,
        content={'message': 'Student added successfully'}
    )
    