# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;

# ... #

def delete_event( widget, data ):
	return False;

def destroy( widget, data = None ):
	gtk.main_quit();

# ... #

window = gtk.Window( gtk.WINDOW_TOPLEVEL );

window.set_title( "مرحباً بالعالم" );
window.connect( 'delete_event', delete_event );
window.connect( 'destroy', destroy );

# ... #

hello_world_button = gtk.Button( "مرحباً بالعالم" );
hello_world_button.show();

# ... #

window.add( hello_world_button );

window.show();

gtk.main();
