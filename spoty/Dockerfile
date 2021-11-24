# Run audithon in a container
#
# docker run --device /dev/snd:/dev/snd --group-add $(getent group audio | cut -d: -f3) --name pyaudio audithon:0.1 
# docker build -t audithon:0.1 .

FROM ubuntu:20.04

ENV HOME /home/admin

RUN	apt-get update && apt-get install -y \
  python3 python3-pip \ 
  python3-pyaudio alsa-utils alsa-base pulseaudio \
	--no-install-recommends && \
  pip install pyaudio wave && \
  groupadd devops && \ 
  useradd -m admin -G devops

USER admin

COPY --chown=admin:devops . $HOME/app

WORKDIR $HOME/app

ENTRYPOINT [ "python3", "redfile.py", "test.wav" ]