#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node Node;

struct node{

    // variable declare
    int data;
    Node *nextNode;

    // function declare
    void (*insert)(Node *,int *);
    bool (*is_data_existing)(Node *, int *);
    void (*print_all)(Node *);
    void (*pop_back)(Node *);
    bool (*is_empty)(Node *);
    void (*reverse_list)(Node *);
    int (*get_list_length)(Node *);
    void (*clear_list)(Node *);
    void (*pop_front)(Node *);
    void (*delete_data)(Node *, int *);
    Node* (*get_last_node_address)(Node *);
};

void insert(Node node, int *data){
    Node* last_node = node.get_last_node_address(&node);
    Node* new_node = (Node*)malloc(sizeof(Node));
    (*new_node).data = data;
    (*new_node).nextNode = NULL;
    (*last_node).nextNode = new_node;

}

void print_all(Node node){
    if(node.is_empty(&node)){
        printf("The list is empty\n");
        return;
    }
    Node* current;
    current = node.nextNode;
    while(current != NULL){
        printf("%d ",(*current).data);
        current = (*current).nextNode;
    }
    printf("\n");
}

bool is_data_existing(Node node, int target_data){
    if(node.is_empty(&node)){
        return false;
    }

    Node* current;
    current = node.nextNode;
    while(current != NULL){
        if((*current).data == target_data){
            return true;
        }
        current = (*current).nextNode;
    }
    return false;

}

void pop_back(Node node){
    if(node.is_empty(&node)){
        return;
    }
    Node* last = node.get_last_node_address(&node);
    free(last);
    if(node.nextNode == last){
        node.nextNode = NULL;
        return;
    }
    Node* current = node.nextNode;
    while((*current).nextNode != last){
        current = (*current).nextNode;
    }
    (*current).nextNode = NULL;

}

Node* get_last_node_address(Node node){
    Node* current;
    if(node.is_empty(&node)){
        current = &node;
        return current;
    }
    current = node.nextNode;
    while((*current).nextNode != NULL){
        current = (*current).nextNode;
    }
    return current;

}

bool is_empty(Node node){
    if(node.nextNode == NULL){
        return true;
    }
    return false;
}

void reverse_list(Node node){
    if(node.is_empty(&node) || node.get_list_length(&node) == 1){
        return;
    }
    Node* current = node.nextNode;
    Node* current_next = (*current).nextNode;
    Node* previous;
    (*current).nextNode = NULL;
    previous = current;
    current = current_next;
    while((*current).nextNode != NULL){
        current_next = (*current).nextNode;
        (*current).nextNode = previous;

        previous = current;
        current = current_next;

    }
    (*current).nextNode = previous;
    node.nextNode = current;



}

void clear_list(Node node){
    while(node.nextNode!=NULL){
        node.pop_back(&node);
    }
}

int get_list_length(Node node){ // not include head
    if(node.is_empty(&node)){
        return 0;
    }
    Node* current;
    current = node.nextNode;
    int length = 1;
    while((*current).nextNode != NULL){
        current = (*current).nextNode;
        length++;
    }
    return length;

}

void pop_front(Node node){
    if(node.is_empty(&node)){
        return;
    }
    Node* temp;
    temp = (*(node.nextNode)).nextNode;
    free(node.nextNode);
    node.nextNode = temp;


}

void delete_data(Node node, int target_data){
    if(node.is_empty(&node)){
        return;
    }

    Node* current;
    Node* previous = &node;
    current = node.nextNode;
    while(current != NULL){
        if((*current).data == target_data){
            (*previous).nextNode = (*current).nextNode;
            free(current);
            current = (*previous).nextNode;
            continue;
        }
        previous = current;
        current = (*current).nextNode;
    }


}

void initialize(Node* linked_list){
    (*linked_list).nextNode = NULL;
    (*linked_list).insert = insert;
    (*linked_list).print_all = print_all;
    (*linked_list).is_data_existing = is_data_existing;
    (*linked_list).get_last_node_address = get_last_node_address;
    (*linked_list).pop_back = pop_back;
    (*linked_list).is_empty = is_empty;
    (*linked_list).reverse_list = reverse_list;
    (*linked_list).get_list_length = get_list_length;
    (*linked_list).clear_list = clear_list;
    (*linked_list).pop_front = pop_front;
    (*linked_list).delete_data = delete_data;
}


int main(){
    Node linked_list;
    initialize(&linked_list);
    int i;
    for(i = 1; i <= 1024; i*=2){
        linked_list.insert(&linked_list,i);
    }

    linked_list.print_all(&linked_list);
    linked_list.reverse_list(&linked_list);
    linked_list.pop_back(&linked_list);
    linked_list.pop_front(&linked_list);
    linked_list.delete_data(&linked_list,128);

    linked_list.print_all(&linked_list);

    return 0;
}
