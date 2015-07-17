#!/usr/bin/env python
# -*- coding: utf-8 -*-

import github3

user = "zzKuRtzz"
password = "85a4db63"
token = 'test'

# from github3 import GitHub
gh = github3.login(user, password)
# gh = github3.GitHub(token=token)
# gh = github3.GitHub(user, token=token)

repo = gh.repository(user, 'deploy_test')

print repo.

# for repository in gh.iter_all_):
#     print(repository)
    # print('{0} - id: {0.id}, url: {0.html_url}'.format(repository))

#  for repository in gh.iter_all_repos():
#     print('{0} - id: {0.id}, url: {0.html_url}'.format(repository))

# from github3 import login, GitHub
# from getpass import getpass, getuser
# import sys
#
# try:
#     import readline
# except ImportError:
#     pass
#
# try:
#     user = raw_input('GitHub username: ')
# except KeyboardInterrupt:
#     user = getuser()
#
# password = getpass('GitHub password for {0}: '.format(user))
#
# # Obviously you could also prompt for an OAuth token
# if not (user and password):
#     print("Cowardly refusing to login without a username and password.")
#     sys.exit(1)
#
#
# g = login(user, password)
#
# print g






# urlGit = ""
# data = urllib.urlencode({'name': 'zzKuRtzz', 'pass': '123'})
# request = urllib.request.Request(url, data, headers)
# request.get_method = lambda: method
# response = urllib.request.urlopen(request)
# print response.read()

# print "Deploy"