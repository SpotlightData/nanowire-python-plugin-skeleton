# -*- coding: utf-8 -*-

# Example plugin template

import json
import example_plugin_functions as epf

# The function which the plugin is bound to


def main(metadata, jsonld, url):

    ######################
    ### YOUR CODE HERE ###
    ######################
    result_text = epf.example_function(jsonld["text"])

    jsonld["text"] = result_text

    return jsonld


# metadata field is blank since it is not used in this example. Within the system metadata will always be used
metadata = {}
jsonld = {}
jsonld["text"] = "An example"

url = None

output_jsonld = main(metadata, jsonld, url)

print(json.dumps(output_jsonld))
