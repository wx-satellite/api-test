from mitmproxy import http
from mitmproxy import ctx


def request(flow):
    request = flow.request
    info = ctx.log.info
    info(request.url)
    info(str(request.headers))
    info(str(request.cookies))
    info(request.host)
    info(request.method)
    info(str(request.port))
    info(request.scheme)
    info(request.form)


def response(flow):
    response = flow.response
    info = ctx.log.info
    # info(str(response.status_code))
    # info(str(response.headers))
    # info(str(response.cookies))

    headers = response.headers
    content_type = headers["Content-Type"]
    if "image" in content_type:
        print("是图片")
    if "application/json" == content_type:
        print("是json结果")
        print(response.text)
