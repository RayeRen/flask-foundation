from flask import request, jsonify


def configure_global_interceptor(app):
    @app.after_request
    def add_cors_nec_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

    @app.before_request
    def cors_options_allowed():
        if request.method == "OPTIONS":
            response = jsonify()
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, \
                Origin, Accept,Authorization"
            response.headers["Access-Control-Max-Age"] = "120"
            return response
