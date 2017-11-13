#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system, chdir

system("psql -d openstreetmap -c \"CREATE EXTENSION btree_gist\"")
chdir("/root/openstreetmap-website/db/functions/")
system("whoami && pwd")
system("make")

system("psql -d openstreetmap -c \"CREATE FUNCTION maptile_for_point(int8, int8, int4) RETURNS int4 AS '/root/openstreetmap-website/db/functions/libpgosm', 'maptile_for_point' LANGUAGE C STRICT\"")
system("psql -d openstreetmap -c \"CREATE FUNCTION tile_for_point(int4, int4) RETURNS int8 AS '/root/openstreetmap-website/db/functions/libpgosm', 'tile_for_point' LANGUAGE C STRICT\"")
system("psql -d openstreetmap -c \"CREATE FUNCTION xid_to_int4(xid) RETURNS int4 AS '/root/openstreetmap-website/db/functions/libpgosm', 'xid_to_int4' LANGUAGE C STRICT\"")
