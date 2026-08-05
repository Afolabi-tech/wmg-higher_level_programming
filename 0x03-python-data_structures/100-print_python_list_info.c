#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: Pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *list;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n",
			i,
			Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
