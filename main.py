from fastapi import FastAPI
import json

app = FastAPI()

with open('./data.json') as f:
    data = json.load(f)

@app.get('/')
async def hello_world():
    return "Hello, World!"



# get all the students
@app.get('/students')
async def get_students(pref: str = None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data


# get the students by their id
@app.get('/students/{id}')
async def get_student(id: int):
    for student in data:
        if student['id'] == id:
            return student
    return {"error": "Student not found"}


# ex 1
@app.get('/stats')
async def get_stats():

    meal_count = {}
    programme_count = {}

    for student in data:

        #meal
        pref = student['pref']
        if pref in meal_count:
            meal_count[pref] += 1
        else:
            meal_count[pref] = 1

        # programmes
        programme = student['programme']
        if programme in programme_count:
            programme_count[programme] += 1
        else:
            programme_count[programme] = 1

    # results
    stats = {}

    for key in meal_count:
        stats[key] = meal_count[key]

    for key in programme_count:
        stats[key] = programme_count[key]

    return stats



# ex 2
@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return {"result": a + b}


@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return {"result": a - b}


@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return {"result": a * b}


@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}
