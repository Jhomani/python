# docker build -t tkinterapp .
# docker run -ti --net=host -e DISPLAY -v /tmp/.X11-unix tkinterapp sh 

FROM alpine:3.14

# LABEL maintainer="jhomanidev@gmail.com"
# LABEL version="0.1"
# LABEL description="Custom Docker Image for python audio"

RUN apk add --no-cache xauth mousepad

RUN addgroup -S swali && \
    adduser -S admin -G swali -s /bin/sh && \
    apk add --no-cache
    # pip3 install tk 

USER admin

COPY --chown=admin:swali . home/admin/app
WORKDIR /home/admin/app

EXPOSE 8887

# Commands to run Tkinter application
CMD mousepad 