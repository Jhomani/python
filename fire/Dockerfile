# xauth list   // then copy the following coockie: <username>/unix:  MIT-MAGIC-COOKIE-1  f1fa006c1e51fa8386209f85c57947c4
# docker build -t <image-name> .
# docker run -it --net=host -e DISPLAY -v /tmp/.X11-unix guitest bash  // into machice run
#$ xauth add <cookie>  // to add cookie
#$ xauth list   // to verify
#$ firefox // to run firefox into localmachine

FROM ubuntu:latest

# ENV TZ='America/Los_Ange'

# RUN ls /usr/share/zoneinfo
# RUN cp /usr/share/zoneinfo/${TZ} /etc/localtime && \
#     echo ${TZ} >  /etc/timezone

RUN apt-get -y update && \ 
    apt-get -y install xauth python3.9 \
    python3-tk python3-pip


RUN addgroup -S swali && \
    adduser -S admin -G swali -s /bin/sh && \
    pip3 install tk 

USER admin

COPY --chown=admin:swali . home/admin/app
WORKDIR /home/admin/app

EXPOSE 8887
CMD ["python3", "tk.py"] 