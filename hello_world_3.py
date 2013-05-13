# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;

def delete_event( widget, data ):
	return False;

def destroy( widget, data = None ):
	gtk.main_quit();

def the_new_window( widget,data = None ):
	new = gtk.Window();
	new.set_title( "نافذتنا الجديده" );
	
	msg = gtk.Label( "هذا برنامجي الاول مع PyGTK" );
	msg.show();
	
	new.add( msg );
	
	new.show();

# ... #

window = gtk.Window();

# ... #

window.set_title( "مرحباً بالعالم" );
window.connect( 'delete_event', delete_event );
window.connect( 'destroy', destroy );

# ... #

box1 = gtk.HBox();
window.add( box1 );

# ... #

hello_world_button = gtk.Button( "مرحباً بالعالم" );
hello_world_button.connect( 'clicked', the_new_window ); # New line
box1.pack_start( hello_world_button );
hello_world_button.show();

# ... #

hello_world_button_2 = gtk.Button( "الزر الثاني" ); 
box1.pack_start( hello_world_button_2 );
hello_world_button_2.show();

# ... #

box1.show();
window.show();

gtk.main();

