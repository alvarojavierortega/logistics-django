 FROM python:slim as dependency
 WORKDIR /reqs
 COPY requirements.txt .
 RUN pip install -r requirements.txt
 
 FROM python:slim
 WORKDIR /home/app
 COPY --from=dependency /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages/
 COPY . .