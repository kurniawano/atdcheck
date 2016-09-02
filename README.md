# atdcheck
Python wrapper for checking using ATD (After the Dateline). Please see the following websites:
* [ATD API](http://www.afterthedeadline.com/api.slp)
* [after_the_dateline Python Wrapper](https://bitbucket.org/miguelventura/after_the_deadline/wiki/Home)

# Installation
To install use PIP.
```bash
pip install atdcheck
```

# How To Use
To check a text file:
```bash
atdcheck mytextfile.txt
```
or if you have generated a key for the API, you can also do:
```bash
atdcheck --key mykey mytextfile.txt
```

