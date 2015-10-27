#!usr/bin/env python3
# -*- coding:utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        self._width=value
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height
