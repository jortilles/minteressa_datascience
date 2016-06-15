<<<<<<< HEAD
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
=======
FROM cmfatih/phantomjs

RUN apt-get -y update
RUN apt-get install python-pip
sudo apt-get install nodejs
RUN pip install --upgrade pip
RUN pip install builtwith
>>>>>>> master
RUN pip install python-whois
RUN pip install html5lib
RUN pip install requests
RUN pip install selenium
<<<<<<< HEAD
RUN pip install pymongo
#RUN brew install phantomjs
#RUN pip install pil


RUN mkdir -p /tmp/c


RUN mkdir -p /usr/scrapping
ADD ./scrapping /usr/scrapping
RUN chmod u+x /usr/scrapping/run.sh

WORKDIR /usr/scrapping

CMD [ "/usr/scrapping/run.sh", "start" ]
=======






RUN mkdir -p /usr/scrapping/phantom/
ADD . /usr/scrapping/
RUN chmod u+x /usr/scrapping/phantom/printUrl.sh

WORKDIR /usr/scrapping/phantom/
# working with local copy. You can get the original from: 
# RUN wget https://github.com/ariya/phantomjs/raw/master/examples/rasterize.js
ADD . /usr/scrapping/



CMD [ "/usr/scrapping/phantom/printUrl.sh", "start" ]
>>>>>>> master

