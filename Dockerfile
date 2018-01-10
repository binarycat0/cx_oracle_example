FROM binarycat/cx_oracle:5

RUN pip install pony
RUN pip install flask


WORKDIR /app
ADD . /app

ENV FLASK_APP /app/test_cx_oracle.py

EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0","--port=80"]
