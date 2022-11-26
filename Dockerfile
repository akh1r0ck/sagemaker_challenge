FROM python:3.8.15

ARG WORKINGDIR="/workspace/"

# RUN apt-get -y update && apt-get install -y --no-install-recommends \
#         g++ \
#         make \
#         cmake \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update
# RUN apt-get install -y python3-pip
RUN python -m pip install --upgrade pip
RUN pip install fastapi uvicorn[standard]
RUN pip install pandas
RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install simpletransformers

WORKDIR ${WORKINGDIR}
RUN mkdir -p ${WORKINGDIR}
COPY src/app.py ${WORKINGDIR}
COPY src/best_model/ ${WORKINGDIR}best_model/

ENTRYPOINT [ "/usr/local/bin/python", "app.py"]