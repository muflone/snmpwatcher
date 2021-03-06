##
#     Project: SNMP Watcher
# Description: Watch devices through SNMP
#      Author: Fabio Castelli (Muflone) <muflone@vbsimple.net>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import pysnmp.smi.rfc1902
from pysnmp.proto.rfc1905 import noSuchObject


class SNMPValue(object):
    """SNMPValue object containing value name, SNMP oid and its value.

    The name will contain a pure clean OID as obtained from a SNMPGET response,
    while the meta_oid will contain the original OID before any substitution"""
    def __init__(self, meta_oid, name, value):
        self.name = name
        self.meta_oid = meta_oid
        if isinstance(value, pysnmp.smi.rfc1902.ObjectType):
            self.oid = value[0].prettyPrint()
            self.value = value[1].prettyPrint()
        else:
            self.oid = None
            self.value = value

    def __repr__(self):
        """Show the instance values"""
        return '<%s object name: %s (%s) = Value: %s>' % (
            self.__class__.__name__,
            self.name,
            self.oid,
            self.value)

    def is_valid(self):
        """Return True if the value is not a noSuchObject error"""
        return self.value != noSuchObject.prettyPrint()
