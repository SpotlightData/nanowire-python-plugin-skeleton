#Initialise the docker container by grabbing the official python repo. Advanced users may like to use their own custom repos to reduce build time
FROM python:3.6

#install the python libraries that your plugin requires
ADD requirements.txt /
RUN pip3 install -r /requirements.txt

ADD example_plugin_template.py /

CMD ["python3", "/example_plugin_template.py"]