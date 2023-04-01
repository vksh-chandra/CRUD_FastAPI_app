from fastapi import APIRouter


router = APIRouter(
    tags=['Home'],
)

@router.get('/', status_code=200)
def get_all():
    return {"Message": "Go to => /docs, after link to access API and enjoy!!"}
