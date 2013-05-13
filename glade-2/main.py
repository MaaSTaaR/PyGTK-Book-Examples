# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;

# ... #

def delete_event( widget, data ):
	return False;

def destroy( widget, data = None ):
	gtk.main_quit();
	
def clickEvent( widget, data = None ):
	global text_entry,status_label;
	
	val = text_entry.get_text();
	val = float( val );
	
	result = ( val * 1.8 ) + 32;
	result = str( result );
	
	status_label.set_text( result );

def keyEvent( widget, data ):
	key = gtk.gdk.keyval_name( data.keyval );
	
	if ( key == 'Return' ):
		clickEvent( None );

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

window = builder.get_object( 'window1' );
text_entry = builder.get_object( 'entry1' );
status_label = builder.get_object( 'label1' );

signals = {	"clickEvent" : clickEvent,
			"keyEvent" : keyEvent,
			"destroy" : destroy,
			"delete_event" : delete_event}

builder.connect_signals( signals );

window.show();

gtk.main();
