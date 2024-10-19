FROM ubuntu:22.04

ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt-get update && apt-get -y install sudo

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME
RUN chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

RUN sudo apt-get -y install software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt-get -y update
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -y install python3.12
RUN sudo apt-get -y install python3-pip
RUN sudo apt install -y python3-pyqt5
RUN sudo apt install -y python3-pyqt5.qtmultimedia
RUN sudo apt install -y postgresql
RUN sudo apt-get install -y libpq-dev
RUN sudo apt-get install -y libqt5multimedia5-plugins
RUN sudo apt-get install -y curl

WORKDIR /app

COPY docker/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# ENTRYPOINT ["src/scripts/entrypoint.sh"]
ENTRYPOINT ["/bin/bash"]