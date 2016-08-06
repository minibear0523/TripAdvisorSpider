# encoding=utf-8
"""
Topic: Fabric Automatic Deploy File
Desc: 
"""
from fabric.api import local


def prepare_deploy():
    local('git add --all && git commit')
    local('git push')

