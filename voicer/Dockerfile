# RUN AS
#
# docker build -t pythonimg:0.1 .
# docker run --device /dev/snd:/dev/snd --group-add $(getent group audio | cut -d: -f3) --name alpitest pythonimg:0.1

FROM alpine:3.14

LABEL maintainer="jhomanidev@gmail.com"
LABEL version="0.1"
LABEL description="Custom Docker Image for python audio"

RUN addgroup -S swali && \
    adduser -S admin -G swali -s /bin/sh && \
    apk add --no-cache python3 py3-pip py3-pyaudio alsa-utils && \
    pip3 install pyaudio wave

USER admin

COPY --chown=admin:swali . home/admin/app
WORKDIR /home/admin/app

# ENV HOST=0.0.0.0 PORT=3000

# EXPOSE ${PORT}/tcp
# ENTRYPOINT [ "aplay", "test.wav" ]
ENTRYPOINT [ "python3", "redfile.py", "test.wav" ]


