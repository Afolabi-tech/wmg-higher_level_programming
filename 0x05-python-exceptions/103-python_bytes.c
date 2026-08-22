#include "lists.h"
#include <stdio.h>

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

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [X] Not a valid Python bytes object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(p);

	printf("[.] bytes object info\n");
	printf("  - size: %ld\n", (long)size);

	if (size > 10)
		limit = 10;
	else
		limit = size;

	printf("  - trying string: %s\n", bytes->ob_sval);
	printf("  - first %ld bytes: ", (long)limit);

	for (i = 0; i < limit; i++)
	{
		printf("%02x", (unsigned char)bytes->ob_sval[i]);

		if (i < limit - 1)
			printf(" ");
	}

	printf("\n");
}
