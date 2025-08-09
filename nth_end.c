#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
void push(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    *head_ref = new_node;
}
int getNthFromEnd(struct Node* head, int n) {
    struct Node* main_ptr = head;
    struct Node* ref_ptr = head;
    int count = 0;
    while (count < n) {
        if (ref_ptr == NULL) return -1;
        ref_ptr = ref_ptr->next;
        count++;
    }
    while (ref_ptr != NULL) {
        main_ptr = main_ptr->next;
        ref_ptr = ref_ptr->next;
    }
    return main_ptr->data;
}
int main() {
    struct Node* head = NULL;
    push(&head, 20);
    push(&head, 4);
    push(&head, 15);
    push(&head, 35);
    int n = 2;
    printf("Nth node from end is %d\n", getNthFromEnd(head, n));
    return 0;
}
