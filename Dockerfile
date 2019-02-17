FROM redrime/rime-compositor:1
RUN mkdir /latex
WORKDIR /latex
ADD . /latex
CMD ["python3", "Rimu.py"]
