# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;
import gtk.glade;
from pysqlite2 import dbapi2 as sql;

def delete( widget, data ):
	return False;

def des( widget, data = None ):
	gtk.main_quit();

def addNewName( widget, data = None ):
	global entry, status, con, cur, store;
	
	name = entry.get_text();
	
	if ( not name ):
		status.set_text( 'يرجى كتابة الاسم المطلوب' );
	else:
		insert = cur.execute( 'INSERT INTO names(id,name) VALUES(NULL,"' + name + '")' );
		
		check = con.commit();
		
		if check == None:
			status.set_text( 'تم اضافة الاسم بنجاح' );
			entry.set_text( '' );
			store.append( [ name ] );
			
con = sql.connect( 'sqlite_db' );
cur = con.cursor();

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

window = builder.get_object( 'window1' );
tree = builder.get_object( 'treeview1' );
entry = builder.get_object( 'entry1' );
status = builder.get_object( 'label2' );

signals = {	"addNewName" : addNewName,
			"des" : des,
			"delete" : delete}

builder.connect_signals( signals );


# ... #


col = gtk.TreeViewColumn( 'الاسم', gtk.CellRendererText(), text = 0 );

tree.append_column( col );

# ... #

store = gtk.ListStore( str );

tree.set_model( store );

# ... #

get_names_query = cur.execute( "SELECT * FROM names" );
names = cur.fetchall();

if len( names ) > 0:
	k = 0;
	while k < len( names ):
		store.append( [ names[ k ][ 1 ] ] );
		
		k += 1;

# ... #

window.show();

gtk.main();
