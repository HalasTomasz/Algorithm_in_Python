#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>


struct List{
    int number;
    struct List* next;
    struct List* back;
};

int size=0;

void prepare(struct List **root) {

    if (*root == NULL) {
        *root = (struct List *) malloc(sizeof(struct List *));
        (*root)->number = rand() % 5;;
        (*root)->next = (*root)->back = (*root);
        return;
    }
}

void add(struct List **root){

    if(size == 0){
        prepare(root);
    }
    else {

        struct List *cur = (struct List *) malloc(sizeof(struct List *));
        cur->number=rand() % 5;

        struct List *tmp1 = (*root)->back;
        (*root)->back = cur;
        cur->next = *root;
        cur->back = tmp1;
        tmp1->next = cur;
        if (size == 1) (*root)->next = cur;
    }
    size++;
}


void read(struct List *root){
  if(!root) printf("%d",root->number);
  struct List *tmp=root;
  if(size!=0) {
      for (int i = 1; i <= size; i++) {
          printf("%d", tmp->number);
          tmp = tmp->next;
      }
  }
}

void find(struct List *list1, int data,bool type){
    if(size==0) return;
    else {
        if (type == true) {
        struct List *tmp = list1;
        int i = 0;
        while (data > i && i < size) {
            tmp = tmp->next;
            i++;
        }
        if (i == data) return;
        else printf("No Space");
        }
        else{
            struct List *tmp = list1;
            int i = 0;
            while (data > i && i < size) {
                tmp = tmp->back;
                i++;
            }
            if (i == data) return;
            else printf("No Space");
        }
    }
}
struct List *merge(struct List **list1, struct List **list2){

    struct List* tmp = (*list1);
    struct List *tmp1 = (*list2);


    for(int i=0;i<size-1;i++){
        tmp=tmp->next;
        tmp1=tmp1->next;
    }

    tmp->next=(*list2);
    (*list2)->back=tmp;
    tmp1->next=(*list1);
    (*list1)=tmp1->back;

    size=size*2;
}

void delete(struct List **list1, int element){
    struct List* tmp =(*list1);
    struct List* tmp2;

    if(element>size){
        printf("Przekroczono rozmiar");
        return;
    }
    for(int i=0;i<element;i++){
     tmp=tmp->next;
    }
    tmp2=tmp->next;
    tmp2->back=tmp->back;
    tmp->back->next=tmp2;
    free(tmp);
    size--;
}

float NormalTester(struct List  *root,int data) {
    clock_t start, end;
    start = clock();
    for (int i = 0; i < 10000; i++) {
        if(data>500) find(root, data,false);
        else find(root, data,true);
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
        if(number>500) find(root, number,false);
        else find(root, number,true);
    }

    end = clock();
    float time = (float)end - start;
    return time/CLOCKS_PER_SEC;
}

int main() {

    srand(time(0));
    struct List* list1=NULL;
    struct List* list2=NULL;

    for(int i=0;i<1000;i++){
        add(&list1);
    }
    size=size-1000;
    for(int i=0;i<1000;i++){
        add(&list2);
    }
	
    //Show elements of list1
    read(list1);
    printf("\n");

    //Show elements of list2
    read(list2);
    printf("\n");

    //Merge two list into one
    merge(&list1,&list2);
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
    find(list1,5);
    delete(&list1,3);

    return 0;
}
