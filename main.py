#!/usr/bin/env python3

import itertools
import re
import sys

import pandas as pd
import plotly.express as px


usage = "usage: ./main.py <inputfile>"

if len(sys.argv) == 1:
    print(usage)
    sys.exit()


input_filename = sys.argv[1]


def fread(fname):
    with open(fname, 'r') as fp:
        return fp.read()


data = sorted(
    list(itertools.chain.from_iterable([
        re.sub(" ", "", line).split(",") for line in
        fread(input_filename).split("\n")
        if line != ''
    ]))
)

grouped = itertools.groupby(data)
groupmap = {
    key: len(list(group)) for key, group
    in grouped
}

plot_data = sorted(groupmap.items(), key = lambda x: -x[1])
pd_data = pd.DataFrame(plot_data, columns = ['Technology', 'Mentions'])


fig = px.bar(pd_data, x='Technology', y='Mentions')
fig.show()
