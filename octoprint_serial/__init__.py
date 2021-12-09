# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import serial

ser = serial.Serial('/dev/ttyACM0',115200)

class ArmPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Controls 6DOF Arm Movement.")


__plugin_name__ = "Arm Control"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Control Arduino based Robotic arm"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = ArmPlugin()
