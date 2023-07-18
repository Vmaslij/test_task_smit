FROM python:3.8
RUN pip install --upgrade pip && pip install fastapi && pip install "uvicorn[standard]" &&  pip install tortoise-orm
COPY . .
RUN python db_test.py
ENTRYPOINT ["python", "main_smit.py"]
EXPOSE 8000
