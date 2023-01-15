# MICS_W295_Docker_POC
Docker POC to show teammates how to use docker

# Running the python hello world script
You can run the script in a python environment (3.9.16) no matter your OS or the version installed locally (or the absence thereof). You might get a warning running it on a Windows host but that's OK.

use the following commands:

first:

```docker build -t <name-of-your-image> .```

example:

``` docker build -t my-python . ```


then:

``` docker run -it --rm --name <name-of-your-container> <name-of-your-image>  ```

example:

``` docker run -it --rm --name helloworld_python my-python ```