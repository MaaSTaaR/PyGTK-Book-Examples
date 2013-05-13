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

box1 = gtk.HBox(); # New line
window.add( box1 ); # New line

# ... #

hello_world_button = gtk.Button( "مرحباً بالعالم" );
box1.pack_start( hello_world_button ); # New line
hello_world_button.show();

# ... #

hello_world_button_2 = gtk.Button( "الزر الثاني" );  # New line
box1.pack_start( hello_world_button_2 ); # New line
hello_world_button_2.show();  # New line

# ... #

box1.show(); # New line
window.show();

# ... #

gtk.main();
