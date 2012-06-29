from flask import Flask, request, render_template
from scormcloud.client import ScormCloudService
from scormcloud.client import ScormCloudUtilities
from xml.sax.saxutils import escape
from xml.dom import minidom


#-----------------------------
# App Configuration

class Config:
    SC_APP_ID = ""
    SC_SECRET_KEY = ""

    SC_SERVICE_URL = "http://cloud.scorm.com/EngineWebServices"
    SC_ORIGIN = ScormCloudUtilities.get_canonical_origin_string('CareerBuilder',
        'Rescare Academy Management', '1.0')

    SC_SERVICE = ScormCloudService.withargs(Config.SC_APP_ID, Config.SC_SECRET_KEY, Config.SC_SERVICE_URL, Config.SC_ORIGIN)

    SECRET_KEY = 'al40C*Sxzs*@#zppr'
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


#-----------------------------
# App

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/massapply/')
def massapply():
    return render_template('massapply.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
