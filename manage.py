from flask import Flask, flash, request, render_template
from scormcloud.client import ScormCloudService
from scormcloud.client import ScormCloudUtilities


#-----------------------------
# App Configuration

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


#-----------------------------
# App

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/massapply/', methods=['POST', 'GET'])
def massapply():
    if request.method == 'POST':
        config_element = request.form['config_element']
        config_element_value = request.form['config_element_value']

        sc_course_service = Config.SC_SERVICE.get_course_service()
        sc_courses = sc_course_service.get_course_list()
        sc_course_count = sc_courses is not None and len(sc_courses) or 0

        flash('The config settings have been applied to ' + str(sc_course_count) + ' courses.')
    return render_template('massapply.html')


@app.route('/courselist/')
def courselist():
    sc_course_service = Config.SC_SERVICE.get_course_service()
    sc_courses = sc_course_service.get_course_list()
    sc_course_count = sc_courses is not None and len(sc_courses) or 0

    return render_template('courselist.html', courses=sc_courses, courseCount=sc_course_count)


@app.route('/')
def index():
    sc_debug_service = Config.SC_SERVICE.get_debug_service()
    return render_template('index.html', ping=sc_debug_service.ping(), authPing=sc_debug_service.authping())


if __name__ == "__main__":
    app.run()
