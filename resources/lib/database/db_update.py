# -*- coding: utf-8 -*-
"""Database update functions"""
from __future__ import absolute_import, division, unicode_literals

import resources.lib.common as common
from resources.lib.globals import g


def run_local_db_updates(db_version, db_new_version):
    """Perform database actions for a db version change"""
    # The changes must be left in sequence to allow cascade operations on non-updated databases
    if common.is_less_version(db_version, '0.2'):
        pass
    if common.is_less_version(db_version, '0.3'):
        pass
    g.LOCAL_DB.set_value('db_version', db_new_version)


def run_shared_db_updates(db_version, db_new_version):
    """Perform database actions for a db version change"""
    # The changes must be left in sequence to allow cascade operations on non-updated databases
    if common.is_less_version(db_version, '0.2'):
        pass
    if common.is_less_version(db_version, '0.3'):
        pass
    g.LOCAL_DB.set_value('db_version', db_new_version)
