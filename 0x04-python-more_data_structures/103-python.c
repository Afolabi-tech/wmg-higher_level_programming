#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_list - prints basic information about a Python list
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject **items;
	PyListObject *list;

	printf("[*] Python list info\n");

	if (p == NULL)
		return;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);

	printf("[*] Allocated = %ld\n", list->allocated);

	items = list->ob_item;

	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %ld: %s\n", i,
		       items[i]->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints basic information about a Python bytes object
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size;
	Py_ssize_t i;
	Py_ssize_t limit;

	printf("[.] bytes object info\n");

	if (p == NULL || p->ob_type != &PyBytes_Type)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = bytes->ob_base.ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	limit = size < 10 ? size : 10;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);

	printf("\n");
}
