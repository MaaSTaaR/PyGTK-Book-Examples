# -*- coding: utf-8 -*-

import pygtk;
pygtk.require( '2.0' );
import gtk;

# ... #

def delete( widget, data ):
	return False;

def des( widget, data = None ):
	gtk.main_quit();
	
def doMath( widget, data = None ):
	global result_label, first_number, second_number, operation;
	
	operand1 = first_number.get_text();
	operand2 = second_number.get_text();
	op = operation.get_text();
	
	if ( not operand1 or not operand2 or not op ):
		result_label.set_text( "يرجى تعبئة المعلومات المطلوبه" );
	else:
		operand1 = int( operand1 );
		operand2 = int( operand2 );
		
		result = operand1;
		
		if op == "+":
			result += operand2;
		elif op == "-":
			result -= operand2;
		elif op == "*":
			result *= operand2;
		elif op == "/":
			result /= operand2;
		else:
			result_label.set_text( "العمليه التي قمت بإختيارها غير صحيحه" );
			return False;
		
		result_label.set_text( str( result ) );

def keyEvent( widget, data ):
	key = gtk.gdk.keyval_name( data.keyval );
	
	if ( key == 'Return' ):
		doMath( None );
	
# ... #
		
win = gtk.Window();

win.set_title( "آله حاسبه" );
win.connect( 'delete_event', delete );
win.connect( 'destroy', des );

# ... #

main_box = gtk.VBox();
win.add( main_box );

# ... #

box1 = gtk.HBox();

# ... #

first_number = gtk.Entry();
box1.pack_start( first_number );
first_number.show();

# ... #

operation = gtk.Entry();
box1.pack_start( operation );
operation.show();

# ... #

second_number = gtk.Entry();
box1.pack_start( second_number );
second_number.show();

# ... #

first_number.connect( 'key_release_event', keyEvent );
operation.connect( 'key_release_event', keyEvent );
second_number.connect( 'key_release_event', keyEvent );

# ... #

main_box.pack_start( box1 );

box1.show();

# ... #

button = gtk.Button( "أظهر الناتج" );
button.connect( 'clicked', doMath );
main_box.pack_start( button );
button.show();

# ... #

result_label = gtk.Label();
main_box.pack_start( result_label );
result_label.show();

# ... #

main_box.show();

win.show();

gtk.main();
