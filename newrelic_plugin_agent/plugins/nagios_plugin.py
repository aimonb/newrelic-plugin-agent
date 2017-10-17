"""
Desk.com Transformation wrapper for Nagios format scripts

"""
import logging

from newrelic_plugin_agent.plugins import base

LOGGER = logging.getLogger(__name__)


class NagiosPlugin(base.NagiosStatsPlugin):

    """ Get my Unique class path """
    my_file = __file__
    me = my_file.split('/')[-1].split('.')[0]
    GUID = "com.desk.{}".format(me)

    def add_datapoints(self, stats):
        """Add all of the data points for a node """
        for key, val in stats.iteritems():
            self.add_gauge_value(val['label'], val['suffix'], float(val['value'].split(';')[0]))
