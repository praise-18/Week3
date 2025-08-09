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
void removeLoop(struct Node* loop_node, struct Node* head) {
    struct Node *ptr1 = head;
    struct Node *ptr2;
    while (1) {
        ptr2 = loop_node;
        while (ptr2->next != loop_node && ptr2->next != ptr1) {
            ptr2 = ptr2->next;
        }
        if (ptr2->next == ptr1) break;
        ptr1 = ptr1->next;
    }
    ptr2->next = NULL;
}
void detectAndRemoveLoop(struct Node* head) {
    struct Node *slow = head, *fast = head;
    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            removeLoop(slow, head);
            return;
        }
    }
}
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}
int main() {
    struct Node* head = NULL;
    push(&head, 20);
    push(&head, 4);
    push(&head, 15);
    push(&head, 10);

    head->next->next->next->next = head->next; // create loop
    detectAndRemoveLoop(head);
    printList(head);
    return 0;
}
