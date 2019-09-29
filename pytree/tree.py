# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import os
from typing import List

import yaml
from graphviz import Digraph

DOT = Digraph(comment='The Round Table')


class Counter:
    _count = 0

    @classmethod
    def get(cls):
        count = cls._count
        cls._add()
        return count

    @classmethod
    def _add(cls):
        cls._count += 1


class Node:
    def __init__(self, label):
        self.id = str(Counter.get())
        self._children = []
        self.label = label
        self.dot_node = None
        self._rendered = False

    def add_child(self, child: Node):
        self._children.append(child)

    def add_children(self, children: List[Node]):
        for child in children:
            self.add_child(child)

    @classmethod
    def make_nodes(cls, labels):
        return [
            cls(label)
            for label in labels
        ]

    def render(self):
        if self._rendered:
            return

        self.dot_node = DOT.node(name=self.id, label=self.label)
        for child in self._children:
            child.render()
            DOT.edge(self.id, child.id)


class YAMLParser:
    def __init__(self, filename):
        self.content = open(filename).read()
        self.data = yaml.safe_load(self.content)

    def parse(self):
        raw_root = self.data
        root = self.parse_node(raw_root)
        return root

    def parse_node(self, raw_node: dict) -> Node:
        label = raw_node['l']
        node = Node(label)
        raw_children = raw_node.get('ch', [])
        children = [self.parse_node(raw_child) for raw_child in raw_children]
        node.add_children(children)

        return node


def run(filename):
    filename = os.path.abspath(filename)
    yml_parser = YAMLParser(filename)
    root = yml_parser.parse()
    root.render()
    DOT.render('output/round-table.gv', view=True, format='png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="YAML file name")
    args = parser.parse_args()
    run(args.filename)


if __name__ == '__main__':
    main()
