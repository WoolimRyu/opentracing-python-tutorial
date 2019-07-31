import sys
import logging
from jaeger_client import Config
import time


def open_tracing_example(hello_to):
    ## Span 시작
    span = tracer.start_span('say-hello')

    hello_str = 'Hello, %s!' % hello_to
    print(hello_str)

    ## Span 끝
    span.finish()


def open_tracing_example_with_context_manager(hello_to):
    with tracer.start_span('say-hello') as span:
        span.set_tag('hello-to', hello_to)

        hello_str = 'Hello, %s!' % hello_to
        span.log_kv({'event': 'string-format', 'value': hello_str})

        print(hello_str)
        span.log_kv({'event': 'println'})


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer('trace-hello-world')

hello_to = sys.argv[1]
# open_tracing_example(hello_to)
open_tracing_example_with_context_manager(hello_to)

# yield to IOLoop to flush the spans
time.sleep(2)
tracer.close()
