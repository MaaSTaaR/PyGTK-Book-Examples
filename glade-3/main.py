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

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

window = builder.get_object( 'window1' );
first_number = builder.get_object( 'entry1' );
operation = builder.get_object( 'entry2' );
second_number = builder.get_object( 'entry3' );
result_label = builder.get_object( 'label1' );

signals = {	"doMath" : doMath,
			"keyEvent" : keyEvent,
			"des" : des,
			"delete" : delete}

builder.connect_signals( signals );

window.show();

gtk.main();
