# FastAPI

학습된 모델들을 FastAPI를 이용하여 서빙해봅니다.

<br>

# Requirements
* Docker
* PostgreSQL
* 아래의 환경변수들을 설정해주어야 합니다.

<br>

|환경변수|설명|
|---|---|
|AWS_ACCESS_KEY_ID|MinIO 혹은 S3의 Key ID|
|AWS_SECRET_ACCESS_KEY|MinIO 혹은 S3의 Access Key|
|DB_USER|PostgreSQL DB의 User 이름|
|DB_PASSWD|PostgreSQL DB의 password|
|DB_HOST|PostgreSQL DB의 HOST|
|DB_PORT|PostgreSQL DB의 PORT|
|DB_NAME|PostgreSQL DB의 이름|
|MLFLOW_URI|MLFlow의 URL|
|MLFLOW_S3_ENDPOINT_URL|MinIO의 API URL|

<br>

### 설정예시
```
AWS_ACCESS_KEY_ID=user_id
AWS_SECRET_ACCESS_KEY=user_password
DB_USER=postgres
DB_PASSWD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=stock
MLFLOW_URI=http://localhost:5000
MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
```

.env 파일에 위와 같은 형태로 작성 후 실습 폴더(Serving/fastapi/)에 위치시킵니다.(위의 설정값들은 단순한 예시이므로 실제 실습시에는 반드시 사전에 설정했던 값들로 내용을 수정해야 합니다.)

<br>

# 참고자료
[FastAPI 실습 자료](https://docs.google.com/presentation/d/19EZ9p82S167h-DSDxBzSMAk5Atvzcnffk4BUUr2mIKk/edit?usp=sharing)  