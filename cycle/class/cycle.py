#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 00:17:14 2018

@author: hiking
"""

class cycle:
    def __init__(self):
        self.nodes=[]
        self.edges=[]
        self.attributes={}
    def add_node(self,node):
        if node not in self.nodes:
            self.nodes.append(node)
    def add_nodes(self,*args):
        for node in args:
            if node not in self.nodes:
                self.nodes.append(node) 

    def add_edge(self,edge):
        if edge not in self.edges:
            self.edges.append(edge)
        
    def add_edges(self,*args):
        for edge in args:
            if edge not in self.edges:
                self.edges.append(edge)
        
    def add_attribute(self,edge=None,**kwargs):
        if edge==None or edge not in self.edges :return   
        if edge in self.attributes.keys():
            for k,v in kwargs.items():self.attributes[edge][k]=v     
        else: self.attributes[edge]=kwargs
        return
    def find_cycle(self):
        return
    def is_cycle(self,nodes):
        return
c=cycle()
c.add_node('a')
c.add_nodes('b','b','c')
c.add_edge(('a','b'))
c.add_edges(('a','b'),('a','b'),('c','b'))
c.add_edges(('a','e'))
c.add_attribute(('a','b'),weight=1)
c.add_attribute(('c','b'),lenth=1)
c.add_attribute(('c','b'),weight=1,lenth=2)

print(c.nodes,'-----------',c.edges,'-----------',c.attributes)