FROM binarycat/cx_oracle:5

RUN pip install flask pony==0.7

COPY ./test_app /app
WORKDIR /app

ENV FLASK_APP /app/test_cx_oracle.py

EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0","--port=80"]
