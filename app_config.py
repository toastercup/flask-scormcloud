#-----------------------------
# App Configuration
from scormcloud.client import ScormCloudService, ScormCloudUtilities

class Config:
    SC_APP_ID = ""
    SC_SECRET_KEY = ""

    SC_SERVICE_URL = "http://cloud.scorm.com/EngineWebServices"
    SC_ORIGIN = ScormCloudUtilities.get_canonical_origin_string('CareerBuilder', 'Rescare Academy Management', '1.0')

    SC_SERVICE = ScormCloudService.withargs(SC_APP_ID, SC_SECRET_KEY, SC_SERVICE_URL, SC_ORIGIN)

    SECRET_KEY = 'al40C*Sxzs*@#zppr'
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
