# -*- coding: utf-8 -*-

from pysqlite2 import dbapi2 as sql;

con = sql.connect( 'employees' );
cur = con.cursor();

print cur.execute( 'CREATE TABLE names (id int,name varchar(255),salary int,age int)' );
