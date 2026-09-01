#include "Python.h"

/**
 * print_python_string - Prints info about a Python string object
 * @p: PyObject to check and print info about
 */
void print_python_string(PyObject *p)
{
	long int length;
	char *value;

	printf("[.] s.type = str\n");

	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	length = (long int)PyUnicode_GET_LENGTH(p);
	printf("[.] s.length = %ld\n", length);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("[.] s.ascii = 1\n");
	else
		printf("[.] s.ascii = 0\n");

	value = (char *)PyUnicode_AsUTF8(p);
	printf("[.] s.value = %s\n", value);
}
