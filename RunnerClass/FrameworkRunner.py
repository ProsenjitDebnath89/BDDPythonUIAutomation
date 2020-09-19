#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import sys
from behave import __main__ as runner_with_options

import RunnerClass

if __name__ == '__main__':
    sys.stdout.flush()
    # run Behave + BDD + Python code
    featureFilePath = 'C:/Users/prodebna/PycharmProjects1/BDD/Feature/FF.feature'
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)

