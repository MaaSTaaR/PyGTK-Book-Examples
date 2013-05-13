# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;

# ... #

def delete_event( widget, data ):
	False;

def destroy( widget, data = None ):
	gtk.main_quit();

# ... #

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

# ... #

window = builder.get_object( 'main_window' );
button = builder.get_object( 'hello_world_button' );

# ... #

window.show();
button.show();

gtk.main();
