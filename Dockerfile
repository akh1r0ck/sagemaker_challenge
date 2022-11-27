FROM python:3.8.15

ARG WORKINGDIR="/workspace/"

RUN apt-get update
RUN python -m pip install --upgrade pip
RUN pip install fastapi uvicorn[standard]
RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install simpletransformers

WORKDIR ${WORKINGDIR}
RUN mkdir -p ${WORKINGDIR}
COPY src/app.py ${WORKINGDIR}

ENTRYPOINT [ "/usr/local/bin/python", "app.py"]