FROM unico/docker-selenium-hub-phantomjs
#FROM ubuntu



RUN apt-get -y update
RUN apt-get install  -y python-pip
RUN apt-get install -y nodejs
RUN apt-get install -y phantomjs
RUN apt-get install -y python-pip
RUN apt-get install -y python-imaging  python-dev
# RUN apt-get install -y mongodb

RUN pip install --upgrade pip
RUN pip install builtwith
RUN pip install beautifulsoup4
RUN pip install python-whois
RUN pip install html5lib
RUN pip install requests
RUN pip install selenium
RUN pip install pymongo
#RUN brew install phantomjs
#RUN pip install pil


RUN mkdir -p /usr/scrapping
ADD ./scrapping /usr/scrapping
RUN chmod u+x /usr/scrapping/run.sh

WORKDIR /usr/scrapping

CMD [ "/usr/scrapping/run.sh", "start" ]

