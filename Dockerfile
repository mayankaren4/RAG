FROM python:3.11-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /code
COPY . ./backend

RUN pip install -r ./backend/requirements.txt

WORKDIR /code/backend
EXPOSE 1025

CMD  ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1025"]
