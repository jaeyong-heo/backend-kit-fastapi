# backend-kit-fastapi


### 가상환경

가상환경 폴더 만들기
```sh
python -m venv .venv
```

가상환경 실행 (Window)
```sh
.venv\Script\Activate
```

가상환경 실행 (Linux)
```sh
source .venv/bin/activate
```

requiremnets.txt 생성 커맨드
```sh
pip freeze > requirements.txt
```

requiremnets.txt 이용 패키지 설치 커맨드
```sh
pip install --no-cache-dir --upgrade -r requirements.txt
```

# 서버 실행

    python main.py



# uvicorn 종료

taskkill /im uvicorn.exe /f
