# python path
PATH=${PATH}:/Library/Python/2.7/site-packages

if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then
    # pip
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
    export PIP_VIRTUALENV_BASE=$WORKON_HOME
    export PIP_RESPECT_VIRTUALENV=true
    export PIP_REQUIRE_VIRTUALENV=true
    source /usr/local/bin/virtualenvwrapper.sh
fi
