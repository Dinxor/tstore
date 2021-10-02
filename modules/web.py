import os

from flask import Flask, request, send_from_directory
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
app.config['SECRET_KEY'] = '855a4c5bf56127b8'


@app.route('/myip')
def myip():
    # for s in dir(request):
        # print(s)
    return request
#    return str(request.headers.getlist("X-Forwarded-For"))
#    return str(request.__dict__)


@app.route('/temp.html')
def temp():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'temp.html')


@app.route('/static/js/temp.js')
def tempjs():
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'), 'temp.js')


@app.route('/static/js/jquery-1.4.2.min.js')
def jquery():
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'), 'jquery-1.4.2.min.js')


@app.route('/static/js/paho-mqtt.js')
def pahomqtt():
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'), 'paho-mqtt.js')


def web(tt):
    @app.route('/data', methods=['GET'])
    def new_data():
        code = request.args.get('code')
        val = request.args.get('val')
        if code and val:
            print(code, val)
            cnt = tt['web']['cnt']
            direction = tt['web']['target']
            target = tt[direction]['queue']
            target.put(['web', [int(code), int(val)]], block=True)
            cnt +=1
            tt[name].update({'cnt': cnt})
            return 'Ok'
        return 'Bad data'

    name = 'web'
    tt[name].update({'is_working': True})
    tt[name].update({'cnt': 0})

    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()


if __name__ == '__main__':
    web({'web': {}})

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cached_json', '_get_data_for_json', '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', '_parse_content_type', 'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_control_request_headers', 'access_control_request_method', 'access_route', 'application', 'args', 'authorization', 'base_url', 'blueprint', 'cache_control', 'charset', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 'disable_data_descriptor', 'encoding_errors', 'endpoint', 'environ', 'files', 'form', 'form_data_parser_class', 'from_values', 'full_path', 'get_data', 'get_json', 'headers', 'host', 'host_url', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'input_stream', 'is_json', 'is_multiprocess', 'is_multithread', 'is_run_once', 'is_secure', 'json', 'json_module', 'list_storage_class', 'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'origin', 'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'remote_user', 'routing_exception', 'scheme', 'script_root', 'shallow', 'stream', 'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule', 'user_agent', 'values', 'view_args', 'want_form_data_parsed']


#    return str(request.__dict__)
# {'environ': {'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_SOFTWARE': 'gevent/20.0 Python/3.8', 'SCRIPT_NAME': '', 'wsgi.version': (1, 0), 'wsgi.multithread': False, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.errors': <_io.TextIOWrapper name='' mode='w' encoding='cp1251'>, 'SERVER_NAME': 'DESKTOP-ING17QG', 'SERVER_PORT': '80', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/myip', 'QUERY_STRING': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '55796', 'HTTP_HOST': '127.0.0.1', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'wsgi.input': , 'wsgi.input_terminated': True, 'werkzeug.request': }, 'shallow': False, 'cookies': ImmutableMultiDict([]), 'url_rule': myip>, 'view_args': {}, 'url': 'http://127.0.0.1/myip'}
