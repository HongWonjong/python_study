import json
import numpy as np
import re
import requests

dict_string = '{"foo" : "bar", "foo2" : "bar2"}'

dict = json.load(dict_string)
dict