from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    completion_tokens = request.args.get('completion_tokens', '500')
    prompt_tokens = request.args.get('prompt_tokens', '300')
    total_tokens = request.args.get('total_tokens', '1000')

   # Determine if headers and body should be sent
    send_header = request.args.get('send', '') == 'header'
    send_body = request.args.get('send', '') == 'body'

    # Create response body if send:body is requested
    if send_body:
        response_body = f"""{{
   "usage":{{
      "completion_tokens":{completion_tokens},
      "prompt_tokens":{prompt_tokens},
      "total_tokens":{total_tokens}
   }}
}}
"""
    else:
        response_body = ''  # No body if send:body is not requested

    # Create the response object
    response = Response(response_body, content_type='application/json')

    # Add the headers only if send:header is requested
    if send_header:
        response.headers['completion_tokens'] = completion_tokens
        response.headers['prompt_tokens'] = prompt_tokens
        response.headers['total_tokens'] = total_tokens

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
