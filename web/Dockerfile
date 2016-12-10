FROM python:3.5
ENV PYTHONUNBUFFERED 1
ADD Library /Library
RUN pip install -r /Library/requirements.txt
ADD start.sh /
ADD database_check.py /
CMD ["bash","start.sh"]
