#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct List{
    int number;
    struct List* next;
};


void prepare(struct List **root){

    if(*root == NULL){
        *root=(struct List*)malloc(sizeof (struct List*));
        (*root)->number=rand()%5;
        (*root)->next=NULL;
        return;
    }

    struct List *current = *root;
    while(current->next!=NULL){
        current=current->next;
    }
    current->next=(struct List*)malloc(sizeof (struct List*));
    current->next->number=rand()%5;
    current->next->next=NULL;
}

void read(struct List *root){
    if(root==NULL){
        printf("Lista pusta");
        return;
    }
    else if(root->next== NULL) {
        printf("%d ",root->number);
        return;
    }
    else printf("%d ",root->number);
    read(root->next);
}


void merge(struct List *list1, struct List *list2){
    if(list1->next==NULL) list1->next=list2;
    else merge(list1->next,list2);
}

void find(struct List  *root,int data){
    if(root->next== NULL) {
        printf("Lista pusta");
        return;
    }
    struct List *cur =root;

    for(int i=0; i<1000; i++){
        if(cur->number==data){
            break;
        }
        if(cur->next==NULL) {
            printf("Poza rozmiarem listy");
            break;
        }
        cur=cur->next;
    }
}

void delete(struct List **root, int data)
{
    if(data == 0) {
        if (*root == NULL) {
            printf("Error\n");
            return;
        }
        else{
            struct List *tmp=(*root)->next;
          free(*root);
          *root = tmp;
        }
    }
    else
    {
        struct List *current=*root;
        struct List *tmp;

        int i=0;
        while (current->next != NULL && i < data - 1) {
            current=current->next;
            i++;
        }

        tmp = current->next;
        current->next = tmp->next;
        free(tmp);
    }
}

float NormalTester(struct List  *root,int data) {
    clock_t start, end;
    start = clock();
    for (int i = 0; i < 10000; i++) {
        find(root, data);
    }
    end = clock();
    float time = (float)end - start;
    return time/CLOCKS_PER_SEC;
}

float RandomTester(struct List *root){
    clock_t start, end;
    int number = (int)random()%1000;
    start = clock();

    for (int i = 0; i < 10000; i++) {
        find(root, number);
    }

    end = clock();
    float time = (float)end - start;
    return time/CLOCKS_PER_SEC;
}
int main() {

    srand(time(0));

    struct List* list1=NULL;

    struct List* list2=NULL;

    for(int i=0; i<1000;i++){
        prepare(&list1);
        prepare(&list2);
    }
    
    //Show elements of list1
    read(list1);
    printf("\n");

    //Show elements of list2
    read(list2);
    printf("\n");
    
    //Merge two list into one
    merge(list1,list2);
    read(list1);

    printf("\n");
    //Test the time needed to reach a certain element of list
    printf("%f\n",NormalTester(list1,20));
    printf("%f\n",NormalTester(list1,20));
    printf("%f\n",NormalTester(list1,120));
    printf("%f\n",NormalTester(list1,400));
    printf("%f\n",NormalTester(list1,700));

    //Test the time need to reach a random element of list
    printf("%f\n",RandomTester(list1));

    //Basic functionality of the list
    delete(&list1,0);
    read(list1);

    return 0;
}
