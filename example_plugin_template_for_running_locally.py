# -*- coding: utf-8 -*-

#Example plugin template

import json
import example_plugin_functions as epf

# The function which the plugin is bound to
def main(nmo, jsonld, url):


    ######################
    ### YOUR CODE HERE ###
    ######################
    result_text = epf.example_function(jsonld["text"])
    
    jsonld["text"] = result_text
    

    return jsonld
    

nmo = {}
jsonld = {}
jsonld["text"] = "An example"

url = None

output_jsonld = main(nmo, jsonld, url)

print(json.dumps(output_jsonld))