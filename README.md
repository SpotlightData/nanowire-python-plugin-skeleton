# README #

This is a wireframe of a python plugin to help developers create their own plugins for the Nanowire platform.

### How do I get set up? ###

* Open "example\_plugin\_template.py" this python script shows the basic outline of a nanowire plugin. If you would like a version of this file for testing locally without the "bind" function please see "example\_plugin\_template\_for\_running\_locally.py". These scripts attempt to give a basic framework for how you should build your plugin.
* requirements.txt. List the libraries your plugin needs to download from pypi. Please note that pip will install the latest versions of these libraries unless you specify otherwise. For example you might want to load Spacy 1.9 rather than 2.0 as a number of features of Spacy broke with the transition to Spacy 2.0.
* When your plugin builds it will do so by running Dockerfile. In order to understand how to set up the enviroment for your plugin please see the docker documentation at https://docs.docker.com/
* In order to track versions of your plugin you may want to edit the VERSION file in this repo
* When your plugin is converted into a nanowire component you will be asked for a configuation json. An example configuration json can be found in nanowire.json
* The Jenkinsfile is an example of a pipeline used to build your container. This is where you will run your tests if you use Jenkins and deploy to nanowire.

### Contribution guidelines ###

Please send improvement suggestions to supprt@spotlightdata.co.uk
