from string import ascii_uppercase
import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

# (;FF[4] (;B[aa];W[ab]) (;B[dd];W[ee]))
# '(;A[B])'

def parse(input_string):
    if input_string in ['', '()', ';']:
        raise ValueError('Not a node.')
    # if '[' not in input_string:
    #     raise ValueError('No nodes.')

    parents = {}
    children = {}
    s = re.compile(';[A-Z]{1,2}\[[a-zA-Z]]')
    node_list = s.findall(input_string)
    for node in node_list:
        parents[node[1]] = [node[3]]

    # return all_nodes
    return SgfTree(properties=parents)

print(parse('(;A[B])'))
# print(parse('(;A[B];B[C])'))
# print(parse('(;A[B](;B[C])(;C[D]))'))
# print(parse('(;A[b][c][d])'))
