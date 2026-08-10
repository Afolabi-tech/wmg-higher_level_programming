#include "lists.h"

/** free_dlistint - function that frees the dlistint_t
*@head: pointer to the head of the list
*/
void free_dlistint(dlistint_t *head)
{
    dlistint_t *current;

    while (head != NULL)
    {
        current = head->next;
        free (head);
        head = current;
    }
    
}
