# -*- coding: utf-8 -*-

#Example plugin template

import example_plugin_functions as epf

from nanowire_plugin import bind

# The function which the plugin is bound to. This function will be run on the
#inputs from the pipeline.

#nmo is used for backend tasks and should only be usefull to a few advanced
#users

#jsonld is the object most plugin developers will be interested in as it contains
#the results from previous plugins. These plugins may include text extraction or
#social media scraping meaning that the jsonld will contain the text to be processed
#or the interaction statistics to be examined. If you are creating a plugin which is the
#first in a pipeline this will be "None" and you should create a jsonld to return

#The url is for processing of non-document files. When a plugin is designed to
#process an image or a pdf this url will be a link to that file. The developer should
#grab the image and then perform their processing
def main(nmo, jsonld, url):


    ######################
    ### YOUR CODE HERE ###
    ######################


    return jsonld
    
#The bind function converts your plugin into a server. This means that all you need to worry 
# about is the "main" function and the nanowire-plugin module will handle all of the nanowire
# specific requirements 
bind(main, "plugin-template")