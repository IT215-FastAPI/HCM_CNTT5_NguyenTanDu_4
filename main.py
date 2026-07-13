from fastapi import FastAPI, status, Depends, Request, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db, Base, engoige
from sqlalchemy_utils import create_database, database_exists
from database import DATABASE_URL
from shemas import ClassSection, ClassSectionResponce


if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)

app = FastAPI()

Base.metadata.create_all(bind=engoige)

@app.get("/health", tags=["Health"])
def get_health():
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Ok"
    }

@app.get("/database", tags=["DataBase"])
def get_database(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return{
            "status_code": status.HTTP_200_OK,
            "message": "Ok"
        }
    
@app.get("/class_sections", tags=["Class_sections"], response_model=list[ClassSectionResponce])
def  get_class_sections(
    request: Request,
    db: Session = Depends(get_db)
):
    return  db.query(ClassSection).all()
    
  


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

