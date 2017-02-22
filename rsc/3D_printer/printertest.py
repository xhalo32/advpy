from octoclient.octoclient.client import OctoClient
from pprint import *
import os

f = open( os.path.join(os.path.expanduser('~'), "octoprint_config"), "r" )
apikey = "".join( f.readline(  ).split("\n") )
printer_address = "".join( f.readline(  ).split("\n") )
f.close(  )



oc = OctoClient(url=printer_address, apikey=apikey)

pprint(oc.job_info())