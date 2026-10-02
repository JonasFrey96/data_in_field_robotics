# Data in Field Robotics Website

This directory contains the static website for:

**Data in Field Robotics: From State Estimation to Navigation**

The website entrypoint is `index.html`, and all local assets are stored under `static/`.

## Project structure

- `index.html`: main webpage
- `static/css/`: stylesheets
- `static/js/`: JavaScript files
- `static/images/`: images and logos
- `static/videos/`: video assets

## Local preview

This project is a static website. There is no build step.

### Recommended: `serve.py`

```bash
python3 serve.py          # from the website directory
python3 data_in_field_robotics/serve.py   # or from its parent directory
```

Then open `http://127.0.0.1:8000/`. It always serves the folder `serve.py` lives in, and unlike
`python3 -m http.server` it does not print `BrokenPipeError` tracebacks when the browser cancels a
download (reloads, aborted image requests). Pass a port number to use another port, e.g. `python3 serve.py 8080`.

### Option 1: Serve from the website directory

```bash
cd /home/tutuna/data_in_field_robotics/src/data_in_field_robotics
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/
```

### Option 2: Serve from the repository root

```bash
cd /home/tutuna/data_in_field_robotics
python3 -m http.server 8000 --directory src/data_in_field_robotics
```

Then open:

```text
http://127.0.0.1:8000/
```

## Notes

- Stop the local server with `Ctrl+C`.
- If port `8000` is already in use, replace it with another port such as `8080`.
- If you start the server from the repository root without `--directory`, open `http://127.0.0.1:8000/src/data_in_field_robotics/` instead.
- A `404` request for `/favicon.ico` can be a browser-side automatic request and is usually harmless.
