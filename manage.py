from flask import Flask, flash, request, render_template
import app_config
import sys


#-----------------------------
# App

app = Flask(__name__)
app.config.from_object(app_config.DevConfig)

@app.route('/massapply/', methods=['POST', 'GET'])
def massapply():
    if request.method == 'POST':
        config_element = request.form['config_element']
        config_element_value = request.form['config_element_value']

        sc_course_service = app_config.DevConfig.SC_SERVICE.get_course_service()
        sc_courses = sc_course_service.get_course_list()
        sc_course_count = sc_courses is not None and len(sc_courses) or 0

        if sc_course_count > 0:
            for sc_course in sc_courses:
                try:
                    sc_course_service.update_attributes(courseid=sc_course.courseId, attributePairs={config_element: config_element_value})
                    flash('Course #' + sc_course.courseId + ' updated.')
                except:
                    exception_value = str(sys.exc_info())
                    flash("Unexpected error: %s" % exception_value)
                    flash('Course #' + sc_course.courseId + ' failed.')
            flash('The config settings have been applied to ' + str(sc_course_count) + ' courses.', category='info')
        else:
            flash('No courses found.')

    return render_template('massapply.html')


@app.route('/courselist/')
def courselist():
    sc_course_service = app_config.DevConfig.SC_SERVICE.get_course_service()
    sc_courses = sc_course_service.get_course_list()
    sc_course_count = sc_courses is not None and len(sc_courses) or 0

    return render_template('courselist.html', courses=sc_courses, courseCount=sc_course_count)


@app.route('/')
def index():
    sc_debug_service = app_config.DevConfig.SC_SERVICE.get_debug_service()

    return render_template('index.html', ping=sc_debug_service.ping(), authPing=sc_debug_service.authping())


if __name__ == "__main__":
    app.run()
