
# docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm tkinter_in_docker

# FROM alpine:3.14

# LABEL maintainer="jhomanidev@gmail.com"
# LABEL version="0.1"
# LABEL description="Custom Docker Image for python audio"

# RUN addgroup -S swali && \
#     adduser -S admin -G swali -s /bin/sh && \
#     apk add --no-cache python3 py3-pip tk python3-tkinter && \
#     pip3 install tk 

# USER admin

# COPY --chown=admin:swali . home/admin/app
# WORKDIR /home/admin/app

# # Commands to run Tkinter application
# CMD ["python3", "tk.py"] 

FROM ubuntu:20.04
RUN	apt-get update && apt-get -y install abiword
CMD	abiword