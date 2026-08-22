#include "lists.h"
#include <stdio.h>

/**
 * print_python_list - prints basic information about a Python list
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyList_Check(p))
	{
		printf("[.] list object info\n");
		printf("  [X] Not a valid Python list\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);

	printf("[*] Python list info\n");
	printf("  - size: %ld\n", (long)size);
	printf("  - allocated: %ld\n", (long)list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("  - %ld: %s\n", (long)i,
		       Py_TYPE(list->ob_item[i])->tp_name);
	}
}
