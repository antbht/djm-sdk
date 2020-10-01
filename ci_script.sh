#!/bin/bash

init() {
    echo "Activation of env ..."
    source bin/activate
}

unit_tests() {
    echo "Run unit tests ..."
    python -m unittest unit_tests/*py
}

dist() {
    echo "Build the wheel ..."
    python setup.py bdist_wheel
}


check_exec() {
    if [ $1 != '0' ]; then
        echo "... ko"
        exit $1
    fi;
    echo "... ok"

}

init
check_exec $?
unit_tests
check_exec $?
dist
check_exec $?
