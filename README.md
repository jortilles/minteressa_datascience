# M'interessa scrapping




## Disclaimer

This repository stores one component of broader project code-named "M'interessa" that is expected to evaluate the knowledge acquired in the postgraduate of [Data Science at the Universitat de Barcelona](http://www.ub.edu/datascience/postgraduate/).

This is an ongoing process (at least until version 1.0.0, which is expected to be the one to be presented as a final result).

The links to the repositories of the remaining components will be provided on further releases.



## Objective of the project

The project is intended to use machine learning models, natural language processing and scrapping technologies (along with other big data technologies) to assist the user on choosing and receiving the most relevant tweets that are being distributed over the Twitter public streaming api, given a basic set of tweets provided by the user itself (whether from its timeline or from a twitter search) and from a progressive tweet selection.

The models are expected to learn progressively and specifically for each user's need.

You can read more on the [Link to be provided](#) companion website of the project, explaining the overall details and blog posts from the team members to come.


### Technical requirements

Currently, the only technical requirement is [Docker](https://www.docker.com). The rest of the dependencies are handled by Docker itself inside of each container, and also from the Dockerfile provided into the repository.



## Docker image build


```bash
$ cd src
$ docker build -t minteressa-scrapper .
```

## Docker image run


```bash
$ docker run --name pgds-minteressa-webdb -d mongo:3.2
$  docker run -it  --link pgds-minteressa-webdb:pgds-minteressa-webdb  minteressa-scrapper /bin/bash
```


