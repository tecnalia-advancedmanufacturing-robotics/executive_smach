#!/usr/bin/env python3
import rclpy
import rclpy.node
import smach

__all__ = ['RosState']


class RosState(smach.State):
    """
    A state that can interact with a ROS node.
    """

    def __init__(self, node, **kwargs):
        smach.State.__init__(self, **kwargs)
        self.__node = node

    @property
    def node(self) -> rclpy.node.Node:
        return self.__node
