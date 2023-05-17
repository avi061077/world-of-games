FROM python:alpine3.18
COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./templates/* /app/templates/
COPY ./tests/* /app/tests/
RUN pip install -f requirements.txt
EXPOSE 5000
CMD python MainGame.py




