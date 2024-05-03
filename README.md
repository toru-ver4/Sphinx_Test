# Sphinx Test

## URL

https://toru-ver4.github.io/Sphinx_Test/

## Setup

```PowerShell
docker build -t takuver4/docker:5.3.0 .
docker push takuver4/docker:5.3.0
```

```PowerShell
docker run -it -d -P --name sphinx_for_test -v C:\Users\toruv\OneDrive\work\Sphinx_Test\:/docs --rm takuver4/docker:5.3.0 bash
```

* Attach Visual Studio Code
* Open /docs directory

```bash
sphinx-quickstart
```

* Change `html_theme` to `pydata_sphinx_theme`

```bash
sphinx-autobuild -b html ./sphinx ./docs
```
