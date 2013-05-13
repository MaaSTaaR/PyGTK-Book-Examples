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

def addNewEmp( widget, data = None ):
	add_builder = gtk.Builder();
	add_builder.add_from_file( 'emp.glade' );
	
	add_window = add_builder.get_object( 'window1' );
	emp_name = add_builder.get_object( 'emp_name' );
	salary = add_builder.get_object( 'salary' );
	age = add_builder.get_object( 'age' );
	status = add_builder.get_object( 'status' );
	
	signals = { "Emp" : ( insertEmp, emp_name, salary, age, status ) }

	add_builder.connect_signals( signals );

	add_window.show();

def insertEmp( widget, emp_name, salary, age, status ):
	global store;
	
	name_val = emp_name.get_text();
	salary_val = salary.get_text();
	age_val = age.get_text();
	
	if not name_val:
		status.set_text( 'يرجى كتابة الاسم' );
	elif not salary_val:
		status.set_text( 'يرجى كتابة الراتب' );
	elif not age_val:
		status.set_text( 'يرجى كتابة العمر' );
	else:
		insert = cur.execute( 'INSERT INTO names(id,name,salary,age) VALUES(NULL,"' + name_val + '","' + salary_val + '","' + age_val + '")' );
		
		check = con.commit();
		
		if check == None:
			status.set_text( 'تم اضافة الموظف بنجاح' );
			emp_name.set_text( '' );
			salary.set_text( '' );
			age.set_text( '' );
			store.append( [ name_val, int( salary_val ), int( age_val ) ] );

def updateEmp( widget, data = None ):
	select = tree.get_selection();
	ar = select.get_selected();
	name = ar[ 0 ].get_value( ar[ 1 ], 0 );
	
	info_query = cur.execute( 'SELECT * FROM names WHERE name="' + name + '"' );
	info = cur.fetchall();
	
	edit_builder = gtk.Builder();
	edit_builder.add_from_file( 'emp.glade' );
	
	edit_window = edit_builder.get_object( 'window1' );
	emp_name = edit_builder.get_object( 'emp_name' );
	salary = edit_builder.get_object( 'salary' );
	age = edit_builder.get_object( 'age' );
	status = edit_builder.get_object( 'status' );
	
	signals = { "Emp" : ( editEmp, info[ 0 ][ 1 ], emp_name, salary, age, status ) }

	edit_builder.connect_signals( signals );
	
	emp_name.set_text( info[ 0 ][ 1 ] );
	salary.set_text( str( info[ 0 ][ 2 ] ) );
	age.set_text( str( info[ 0 ][ 3 ] ) );
	
	edit_window.show();
	
def editEmp( widget, old_name, emp_name, salary, age, status ):
	name_val = emp_name.get_text();
	salary_val = salary.get_text();
	age_val = age.get_text();
	
	if not name_val:
		status.set_text( 'يرجى كتابة الاسم' );
	elif not salary_val:
		status.set_text( 'يرجى كتابة الراتب' );
	elif not age_val:
		status.set_text( 'يرجى كتابة العمر' );
	else:
		update = cur.execute( 'UPDATE names SET name="' + name_val + '",salary="' + salary_val + '",age="' + age_val + '" WHERE name="' + old_name + '"' );
		
		check = con.commit();
		
		if check == None:
			status.set_text( 'تم تحديث معلومات الموظف بنجاح' );

	
def deleteEmp( widget, data = None ):
	select = tree.get_selection();
	ar = select.get_selected();
	name = ar[ 0 ].get_value( ar[ 1 ], 0 );
	
	delete = cur.execute( 'DELETE FROM names WHERE name="' + name + '"' );
	
	check = con.commit();
	
	if check == None:
		store.remove( ar[ 1 ] );

con = sql.connect( 'employees' );
cur = con.cursor();

builder = gtk.Builder();
builder.add_from_file( 'gui.glade' );

window = builder.get_object( 'window1' );
tree = builder.get_object( 'treeview1' );
add_emp = builder.get_object( 'button1' );
update_emp = builder.get_object( 'button2' );
delete_emp = builder.get_object( 'button3' );

signals = {	"addNewEmp" : addNewEmp,
			"updateEmp" : updateEmp,
			"deleteEmp" : deleteEmp,
			"des" : des,
			"delete" : delete}

builder.connect_signals( signals );

# ... #

col1 = gtk.TreeViewColumn( 'الاسم', gtk.CellRendererText(), text = 0 );
col2 = gtk.TreeViewColumn( 'الراتب', gtk.CellRendererText(), text = 1 );
col3 = gtk.TreeViewColumn( 'العمر', gtk.CellRendererText(), text = 2 );

tree.append_column( col1 );
tree.append_column( col2 );
tree.append_column( col3 );

# ... #

store = gtk.ListStore( str, int, int );

tree.set_model( store );

# ... #.

get_names_query = cur.execute( "SELECT * FROM names" );
names = cur.fetchall();

if len( names ) > 0:
	k = 0;
	while k < len( names ):
		store.append( [ names[ k ][ 1 ], names[ k ][ 2 ], names[ k ][ 3 ] ] );
		
		k += 1;

# ... #

window.show();

gtk.main();
