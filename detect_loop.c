#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
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
bool detectLoop(struct Node* h) {
    struct Node *slow = h, *fast = h;
    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
int main() {
    struct Node* head = NULL;
    push(&head, 20);
    push(&head, 4);
    push(&head, 15);
    push(&head, 10);
    head->next->next->next->next = head; // create loop
    if (detectLoop(head))
        printf("Loop detected\n");
    else
        printf("No loop\n");
    return 0;
}
