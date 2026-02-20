FROM ubuntu:latest
RUN apt update -y && apt upgrade -y && apt-get install -y texlive-lang-english texlive-luatex fonts-noto fonts-noto-cjk python3 pandoc python3-pip texlive-games texlive-humanities texlive texlive-latex-extra
RUN apt install -y python3-venv
RUN python3 -m venv /VirtEnv
RUN /VirtEnv/bin/pip3 install pypandoc

RUN mkdir /Rimu
WORKDIR /Rimu
ADD Rimu.py /Rimu
CMD ["/VirtEnv/bin/python3", "/Rimu/Rimu.py", "/latex"]
