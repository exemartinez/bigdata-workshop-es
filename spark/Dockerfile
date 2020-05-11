ARG SPARK_VERSION=2.4.5
FROM arjones/spark:${SPARK_VERSION}

WORKDIR /notebook

COPY requirements.txt /tmp/
COPY build_image_igwn.sh /tmp/

RUN chmod 777 /tmp/build_image_igwn.sh && \
    bash /tmp/build_image_igwn.sh

CMD [ "/usr/local/bin/jupyter", "notebook", "--allow-root", "--no-browser", "--ip=0.0.0.0"]

EXPOSE 8888
