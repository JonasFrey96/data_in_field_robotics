#!/usr/bin/env python3
"""Local preview server for the workshop website.

Works like `python3 -m http.server`, but stays quiet when the browser closes a
connection early (on reloads or cancelled image requests). The stock server
prints a BrokenPipeError traceback for those even though nothing is wrong.

Usage (from anywhere; it always serves the folder this file lives in):
    python3 serve.py [port]
"""
import argparse
import functools
import http.server
import os
import sys

CLIENT_DISCONNECTS = (BrokenPipeError, ConnectionResetError, ConnectionAbortedError)


class QuietServer(http.server.ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):
        # Drop client disconnects; report every other error as usual
        if isinstance(sys.exc_info()[1], CLIENT_DISCONNECTS):
            return
        super().handle_error(request, client_address)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("port", nargs="?", type=int, default=8000, help="port to listen on (default: 8000)")
    parser.add_argument("--bind", default="127.0.0.1", help="address to bind to (default: 127.0.0.1)")
    args = parser.parse_args()

    site_dir = os.path.dirname(os.path.abspath(__file__))
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=site_dir)

    with QuietServer((args.bind, args.port), handler) as server:
        print(f"Serving {site_dir} at http://{args.bind}:{args.port}/ (Ctrl+C to stop)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
