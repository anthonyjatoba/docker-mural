FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python banco.py
ENTRYPOINT ["python"]
CMD ["app.py"]
