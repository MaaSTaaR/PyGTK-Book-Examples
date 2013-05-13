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
	
# ... #

window = gtk.Window();

window.set_title( "برنامج التحويل" );
window.connect( 'delete_event', delete_event );
window.connect( 'destroy', destroy );

# ... #

main_box = gtk.VBox();
window.add( main_box );

# ... #

text_entry = gtk.Entry();
main_box.pack_start( text_entry );
text_entry.connect( 'key_release_event', keyEvent );
text_entry.show();

# ... #

status_label = gtk.Label( "" );
main_box.pack_start( status_label );
status_label.show();

# ... #

ok_button = gtk.Button( "موافق" );
main_box.pack_start( ok_button );
ok_button.connect( 'clicked', clickEvent );
ok_button.show();

# ... #

main_box.show();

window.show();

gtk.main();
