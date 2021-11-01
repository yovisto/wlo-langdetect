# WLO Language Detection

A utility and webservice to detect language of text.

The tool is based on the Python [langdetect](https://pypi.org/project/langdetect/) package and wraps a webservice around it.

 
## Prerequisites

- Install [Docker](https://docker.com/).
- Build the Docker container.

```
sh build.sh
```

## Prediction (detect language)

- To test the detection just query the system with an existing document's text.

```
sh runPrediction.sh "Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. The quick brown fox jumps over the lazy dog."
```

The result is a list of languages ([ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)) with a propability score. 

```
en 0.5714256620210416
de 0.4285713688317989
```


## Webservice

- To run the detection tool as a REST based webservice, the following script can be used:

```
sh runService.sh
```

- The scripts deploys a CherryPy webservice in a docker container listening at `http://localhost:8080/langdetect`.

- To retrieve the languages for a given text, create a POST request and submit a json document with a text parameter, e.g.: 

```
curl -d '{"text" : "Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich. The quick brown fox jumps over the lazy dog."}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8080/langdetect
```	

