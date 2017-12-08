# README #

This is a wireframe of a plugin which should work with nanowire. This is designed to help developers create their own plugins.

### What is this repository for? ###

This is a tutorial repo which is designed to help new plugin developers get started building their own plugins. This documentation details development for a system which is as yet unfinished and as such is subject to change however this repo should contain everything you needed to get started. It should also be noted that this documentation is also in an unfinshed state and any suggestions may be folded in at a later stage. If anything is unclear please contact stuart@spotlightdata.co.uk however do not expect a personal response as you suggestions will be rolled into these documents to aid future users.

### How do I get set up? ###

* The first thing you should do is open "example\_plugin\_template.py" this python script shows the basic outline of a nanowire plugin. If you would like a version of this file for testing locally without the "bind" function please see "example\_plugin\_template\_for\_running\_locally.py". These scripts attempt to give a basic framework for how you should build your plugin.
* You should next look at requirements.txt. This is where you should list the libraries your plugin needs to download from pypi. Please note that pip will install the latest versions of these libraries unless you specify otherwise. For example you might want to load Spacy 1.9 rather than 2.0 as a number of features of Spacy broke with the transition to Spacy 2.0.
* When your plugin builds it will do so by running Dockerfile. In order to understand how to set up the enviroment for your plugin please see the docker documentation at https://docs.docker.com/
* In order to track versions of your plugin you may want to edit the VERSION file in this repo
* When your plugin is converted into a nanowire component you will be asked for a configuation json. An example configuration json can be found in nanowire.json
* The Jenkinsfile is an example of a pipeline used to build your container is also given this repo. This is where you will run your tests and deploy to nanowire. In future the jenkinsfile may be abstracted away from the user however for now it is how the system works

### Contribution guidelines ###

If anything in this tutorial seems unclear please contact stuart@spotlightdata.co.uk. I will be unable to reply to your emails directly however your suggestions may be folded into future versions of the repo.

### Who do I talk to? ###

* Stuart@spotlightdata.co.uk
* will@spotlightdata.co.uk