#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}
struct Node* addTwoLists(struct Node* first, struct Node* second) {
    struct Node* res = NULL;
    struct Node** lastPtrRef = &res;
    int carry = 0, sum;
    while (first != NULL || second != NULL) {
        int a = (first) ? first->data : 0;
        int b = (second) ? second->data : 0;
        sum = carry + a + b;
        carry = sum / 10;
        sum = sum % 10;
        *lastPtrRef = newNode(sum);
        lastPtrRef = &((*lastPtrRef)->next);
        if (first) first = first->next;
        if (second) second = second->next;
    }
    if (carry > 0) {
        *lastPtrRef = newNode(carry);
    }
    return res;
}
int main() {
    struct Node* first = newNode(2);
    first->next = newNode(4);
    first->next->next = newNode(3);
    struct Node* second = newNode(5);
    second->next = newNode(6);
    second->next->next = newNode(4);
    struct Node* result = addTwoLists(first, second);
    printf("Sum List: ");
    printList(result);
    return 0;
}
