 #include "main.h"

/**
 * _strspn - gets the length of a prefix substring
 * @s: string to search
 * @accept: characters to look for
 *
 * Return: number of characters in the initial segment of s
 *         that consist only of characters from accept
 */
unsigned int _strspn(char *s, char *accept)
{
	unsigned int i;
	unsigned int j;

	i = 0;

	while (s[i] != '\0')
	{
		j = 0;

		while (accept[j] != '\0')
		{
			if (s[i] == accept[j])
				break;

			j++;
		}

		if (accept[j] == '\0')
			return (i);

		i++;
	}

	return (i);
}
