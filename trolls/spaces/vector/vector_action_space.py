#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy

from trolls.spaces.action_space import ActionSpace

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 9/5/19
           """


class VectorActionSpace:
    """ """

    def __init__(self, action_space: ActionSpace, num_env: int):
        assert isinstance(
            action_space, ActionSpace
        ), f"Action space must be an instance of ActionSpace, was {action_space}"
        self.action_space = action_space
        self.num_env = num_env

    def sample(self) -> numpy.ndarray:
        """

        :return:
        :rtype:
        """
        return numpy.array([self.action_space.sample() for _ in range(self.num_env)])

    def __getattr__(self, item):
        return getattr(self.action_space, item)

    def __repr__(self):
        return self.action_space.__repr__()
