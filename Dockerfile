FROM python:3.8.0-alpine

RUN apk update && apk add \
	bash \
	git \
	git-fast-import \
	make \
	openssh

RUN mkdir /website && chmod 777 /website
COPY requirements.txt /website/
WORKDIR /website

# prevent writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip && \
	pip install -r requirements.txt


# only download the pelican-boostrap3 theme 
RUN mkdir /website/themes \
&& cd /website/themes \
&& git init \
&& git remote add origin -f \
	https://github.com/getpelican/pelican-themes.git \
&& git config core.sparseCheckout true \
&& echo "/pelican-bootstrap3/" >> .git/info/sparse-checkout \
&& git pull origin master 

# only download the i18n_subsites plugin
RUN mkdir /website/plugins \
&& cd /website/plugins \
&& git init \
&& git remote add origin -f https://github.com/getpelican/pelican-plugins \
&& git config core.sparseCheckout true \
&& echo "/i18n_subsites/" >> .git/info/sparse-checkout \
&& git pull origin master

# bust the cache 
WORKDIR /website 
COPY pelicanconf.py /website/ 
COPY publishconf.py /website/
COPY Makefile /website/
