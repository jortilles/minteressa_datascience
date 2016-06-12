FROM cmfatih/phantomjs

RUN apt-get -y update
RUN apt-get install python-pip
sudo apt-get install nodejs
RUN pip install --upgrade pip
RUN pip install builtwith
RUN pip install python-whois
RUN pip install html5lib
RUN pip install requests
RUN pip install selenium






RUN mkdir -p /usr/scrapping/phantom/
ADD . /usr/scrapping/
RUN chmod u+x /usr/scrapping/phantom/printUrl.sh

WORKDIR /usr/scrapping/phantom/
# working with local copy. You can get the original from: 
# RUN wget https://github.com/ariya/phantomjs/raw/master/examples/rasterize.js
ADD . /usr/scrapping/



CMD [ "/usr/scrapping/phantom/printUrl.sh", "start" ]

