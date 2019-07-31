import sys
import opentracing
tracer = opentracing.tracer

def open_tracing_example(hello_to):
    ## Span 시작
    span = tracer.start_span('say-hello')

    hello_str = 'Hello, %s!' % hello_to
    print(hello_str)

    ## Span 끝
    span.finish()


def open_tracing_example_with_context_manager(hello_to):
    with tracer.start_span('say-hello') as span:
        hello_str = 'Hello, %s!' % hello_to
        print(hello_str)


assert len(sys.argv) == 2

hello_to = sys.argv[1]
open_tracing_example(hello_to)
open_tracing_example_with_context_manager(hello_to)
