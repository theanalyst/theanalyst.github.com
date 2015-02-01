Title: Faster python builds in Travis with the container based infra
Date: 2015-02-01
Tags: Python, Travis
Author: Abhishek L
Category: Tech

Lately, travis CI has started supporting builds using [container][1]
based infrastructure which run much faster due to more available
resources and good use of caching. This is currently possible only for
projects that don't use `sudo` atm . For more details read [this][2]
post. Of late, I have been submitting Pull Requests to various
projects to use this feature wherever possible. This post is primarily
oriented towards Python projects.

Commonly if you see travis builds for many python projects, a
significant amount of time just to install the dependencies. So
caching these will save you a good amount of time. Pip downloads can
be cached specifying a cache directory, which will avoid hitting the
pypi mirror for every line in your requirements.

    :::yaml
	- sudo : false
	- cache:
        directories: 
        - $HOME/.pip-cache
	- script:
	    - pip install -r requirements.txt --download-cache $HOME/.pip-cache	
		- make travis


The above lines will make sure that for subsequent runs pip packages
from the cache are used, but still the packages will be built, which
if you're using packages using C, will still mean a lot of time for
building the package itself. One way of working around this would be
the use of Python Wheels and caching them as this avoids the need for
subsequent builds. We could download the wheels to a specified
directory and cache that, so that we can cut down on the build time.
So we would have something like:

    :::yaml
    - sudo : false
	- cache:
        directories: 
        - $PWD/wheelhouse
	- script:
		- pip wheel -r requirements.txt
	    - pip install -r requirements.txt
		- make travis

And voila! We have faster travis builds.

PS If you have better ways to speedup, I'll be happy to hear, please
let me know in comments or hit me up on twitter.

[1] http://blog.travis-ci.com/2014-12-17-faster-builds-with-container-based-infrastructure/
[2] http://docs.travis-ci.com/user/workers/container-based-infrastructure/
