#!/bin/bash

init() {
    source bin/activate
}

unit_tests() {
    python -m unittest unit_tests/*py
}

dist() {
    python setup.py bdist_wheel
}

deploy() {
}

quality() {
}


init
unit_tests
dist
deploy 
quality
