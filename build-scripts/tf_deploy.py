import git
import os
import subprocess
import re
import sys
import json

AWS_DEPLOY_ENVS = ["prod"]
AWS_USE_CASES = ["eks"]

CURRENT_DIR = os.getcwd()
REPO_NAME = os.environ['REPO_NAME']
GIT_DIR = "/build-dir/" + REPO_NAME

if os.path.isdir(GIT_DIR):
    os.chdir(GIT_DIR)
else:
    sys.exit("Not a directory...script exiting")
    

g = git.Git(GIT_DIR)

loginfo = g.log('-1', '--all', '--oneline', '--decorate')
print(loginfo)

COMMIT_ID = subprocess.Popen(['git', 'rev-list', '--tags', '--max-count=1'], stdout=subprocess.PIPE)
COMMIT_ID = COMMIT_ID.stdout.read().strip()

GIT_TAG = subprocess.Popen(['git', 'describe', '--tags', COMMIT_ID], stdout=subprocess.PIPE)
GIT_TAG = GIT_TAG.stdout.read().decode('utf-8').strip()

if re.match(r"[a-z]+?-\d+?.\d+?", GIT_TAG):
    if GIT_TAG.split('-')[0] in AWS_DEPLOY_ENVS:
        BUILD_ENV = GIT_TAG.split('-')[0]
        f = open("/build-dir/build-env.txt", "w")
        subprocess.call(["echo", "export BUILD_ENV=" + BUILD_ENV], stdout=f)
        print(BUILD_ENV)
        f = open("/build-dir/git-tag.txt", "w")
        subprocess.call(["echo", "export GIT_TAG=" + GIT_TAG], stdout=f)
        print(GIT_TAG)
    else:
        sys.exit("Incorrect Git tag format...script exiting")
else:
    sys.exit("Incorrect Git tag format...script exiting")
        
