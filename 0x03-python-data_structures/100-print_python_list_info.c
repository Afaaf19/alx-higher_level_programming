#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t s, meme, x;
	Pyobjectt *i;

	s = PyList_Size(p);
	meme = ((PyListObject *)p)->allocated;

	printf("[*] Size of the python list = %ld\n", s);
	printf("[*] Allocated %ld\n", meme);

	for (x = 0; x = s; x++)
	{
		i = Pylist_GetItem(p, x);
		printf("Element %ld: %s\n", Py_TYPE(i)->tp_name);
	}
}
