#include "lists.h"
#include <stdio.h>

/**
 * print_python_float - prints basic information about a Python float
 * @p: Python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [X] Not a valid Python float object\n");
		return;
	}

	flt = (PyFloatObject *)p;

	printf("  - value: %.17g\n", flt->ob_fval);
}
