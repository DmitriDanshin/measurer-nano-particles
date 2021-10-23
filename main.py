from fastapi import FastAPI, Request, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from handler import handle_image
from schemes import ImageData, ImageCreate
from shutil import copyfileobj

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/dist", StaticFiles(directory="dist/"), name="dist")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
app.mount("/img", StaticFiles(directory="dist/img"), name="img")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")
templates = Jinja2Templates(directory="dist")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_model=ImageData)
def read_image(file: UploadFile = File(...), img: ImageCreate = Depends(ImageCreate)):
    with open("image.png", "wb") as buffer:
        copyfileobj(file.file, buffer)
    image_data = handle_image(params=img)
    return image_data
