FROM python:3.9

RUN mkdir -p /usr/src/app

COPY openleadr-python-main.zip /tmp/

# Use RUN to unzip the archive
RUN unzip /tmp/openleadr-python-main.zip -d /usr/src/app

# Optionally, remove the zip file to save space
RUN rm /tmp/openleadr-python-main.zip

COPY vtn.py /usr/src/app/openleadr-python-main

WORKDIR /usr/src/app/openleadr-python-main

RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -r dev_requirements.txt

CMD [ "python", "vtn.py" ]
EXPOSE 8080