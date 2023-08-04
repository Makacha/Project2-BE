from fastapi import APIRouter
from app.apis.endpoints import user, project, document, work, plan

router = APIRouter()


router.include_router(user.router, prefix="/user", tags=["user"])
router.include_router(project.router, prefix="/project", tags=["project"])
router.include_router(document.router, prefix="/document", tags=["document"])
router.include_router(work.router, prefix="/work", tags=["work"])
router.include_router(plan.router, prefix="/plan", tags=["plan"])
