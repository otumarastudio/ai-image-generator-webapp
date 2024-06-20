# FastAPI와 DALL-E 3를 활용한 이미지 생성 웹 애플리케이션 🎨

이 프로젝트는 FastAPI와 OpenAI의 DALL-E 3 모델을 사용하여 텍스트 입력을 기반으로 이미지를 생성하는 웹 애플리케이션입니다. 사용자는 웹 인터페이스를 통해 텍스트를 입력하고, DALL-E 3 모델이 해당 텍스트를 기반으로 이미지를 생성합니다. 생성된 이미지는 웹 페이지에 표시됩니다.

## 기능 ✨

- 텍스트 입력을 통한 이미지 생성
- DALL-E 3 모델을 활용한 고품질 이미지 생성
- 웹 인터페이스를 통한 사용자 친화적인 경험
- CSS와 JavaScript를 활용한 반응형 디자인

## 사용 기술 🛠️

- FastAPI: 웹 애플리케이션 프레임워크
- OpenAI DALL-E 3: 이미지 생성 AI 모델
- Python: 서버 사이드 프로그래밍 언어
- HTML/CSS: 웹 페이지 구조 및 스타일링
- JavaScript: 클라이언트 사이드 인터랙션 처리

## 설치 및 실행 방법 🚀

1. 이 저장소를 클론하세요.
   ```
   git clone https://github.com/otumarastudio/ai-image-generator-webapp.git
   ```

2. 필요한 패키지를 설치하세요.
   ```
   pip install -r requirements.txt
   ```

3. OpenAI API 키를 설정하세요.
   - `.env` 파일을 생성하고, `OPENAI_API_KEY=your_api_key`와 같이 API 키를 입력하세요.

4. 애플리케이션을 실행하세요.
   ```
   uvicorn main:app --reload
   ```



## 프로젝트 구조 📁

```
.
├── static/
│   ├── index.html
│   ├── favicon.ico
│   └── ...
├── main.py
├── requirements.txt
├── .env
└── README.md
```

- `static/`: 정적 파일(HTML, CSS, JavaScript 등)이 위치한 디렉토리
- `main.py`: FastAPI 애플리케이션 코드
- `requirements.txt`: 필요한 Python 패키지 목록
- `.env`: 환경 변수 파일(OpenAI API 키 저장)
- `README.md`: 프로젝트 설명 문서

## 기여 방법 🤝

1. 이 저장소를 포크하세요.
2. 새로운 브랜치를 생성하세요: `git checkout -b feature/your-feature`
3. 변경 사항을 커밋하세요: `git commit -m 'Add your feature'`
4. 브랜치에 푸시하세요: `git push origin feature/your-feature`
5. 풀 리퀘스트를 열어주세요.

## 라이선스 📄

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다.

---

이 프로젝트를 통해 FastAPI와 DALL-E 3를 활용하여 텍스트 기반 이미지 생성 웹 애플리케이션을 구현하는 방법을 배울 수 있습니다. 코드와 예제를 참고하여 자신만의 아이디어를 구현해 보세요! 😊