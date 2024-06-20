import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI 클라이언트 설정
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

app = FastAPI()

# 정적 파일 제공을 위한 설정
app.mount("/static", StaticFiles(directory="static"),
          name="static")

# 루트 경로(/)에 대한 GET 요청을 처리


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("genimg_static/index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

# 브라우저가 요청하는 favicon.ico 파일 제공


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("genimg_static/favicon.ico")


class TextInput(BaseModel):
    text: str


@app.post("/generate-image")
async def generate_image(input: TextInput):
    text = input.text

    try:
        # OpenAI API 호출
        response = client.images.generate(
            model="dall-e-3",
            prompt=text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return JSONResponse(content={"image_url": image_url})
    except Exception as e:
        print(f"Error: {e}")  # 디버깅을 위한 추가 로그
        raise HTTPException(status_code=500, detail=str(e))
