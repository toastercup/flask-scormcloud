sc-flaskapp
===========

# License
> Software License Agreement (BSD License)
>
> Copyright (c) 2012, CareerBuilder, LLC
> All rights reserved.
>
> Redistribution and use in source and binary forms, with or without
> modification, are permitted provided that the following conditions are met:
>
> *   Redistributions of source code must retain the above copyright
>     notice, this list of conditions and the following disclaimer.
> *   Redistributions in binary form must reproduce the above copyright
>     notice, this list of conditions and the following disclaimer in the
>     documentation and/or other materials provided with the distribution.
> *   Neither the name of the <organization> nor the
>     names of its contributors may be used to endorse or promote products
>     derived from this software without specific prior written permission.
>
> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
> AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
> IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
> DISCLAIMED. IN NO EVENT SHALL CareerBuilder, LLC BE LIABLE FOR ANY
> DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
> (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
> LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
> ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
> (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
> SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Description
This web application provides a simple management frontend for Rustici's SCORM Cloud. It provides rudimentary batch operations for setting configuration values.

## Usage
This is a Flask web app. Please set 'SC_APP_ID' and 'SC_SECRET_KEY' in 'app_config.py'. Run 'manage.py' within its directory, or use gunicorn, uWSGI or similar.

## Dependencies
Depends on Rustici's 'scormcloud' Python library: https://github.com/RusticiSoftware/SCORMCloud_PythonLibrary

Depends on Flask: http://flask.pocoo.org/