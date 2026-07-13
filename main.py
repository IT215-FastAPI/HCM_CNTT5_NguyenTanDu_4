from fastapi import FastAPI, status, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
app = FastAPI()

@app.get("/health", tags=["Health"])
def get_health():
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Ok"
    }

@app.get("/database", tags=["DataBase"])
def get_database(db: Session = Depends(get_db)):
    pass



@app.get("/class_sections", tags=["Class_sections"])
def  get_class_sections(
    request: Request,
    db: Session = Depends(get_db)
):
    return {
        "status_code": status.HTTP_200_OK,
        "message": "API đang chạy",
        "data": [db]
    }



@app.get("/class_sections/{sections_id}", tags=["Class_sections"])
def get_class_sections_by_id():
    pass


@app.get("/class_sections", tags=["Class_sections"])
def get_class_sections_search_subject_name():
    pass

@app.post("/class_sections", tags=["Class_sections"])
def create_class_sections():
    pass

@app.put("/class_sections/{sections_id}", tags=["Class_sections"])
def update_class_sections_by_id():
    pass

@app.delete("/class_sections/{sections_id}", tags=["Class_sections"])
def delete_class_sections_by_id():
    pass

