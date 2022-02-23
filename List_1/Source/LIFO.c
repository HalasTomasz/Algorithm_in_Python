#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct LIFO{
    int number;
    struct LIFO* next;
};

void prepare(struct LIFO **root){

    if(*root == NULL){
        *root=(struct LIFO*)malloc(sizeof (struct LIFO*));
        (*root)->number=rand()%5;
        (*root)->next=NULL;
        return;
    }

    struct LIFO *current = *root;
    while(current->next!=NULL){
        current=current->next;
    }
    current->next=(struct LIFO*)malloc(sizeof (struct LIFO*));
    current->next->number=rand()%5;
    current->next->next=NULL;
}


void read(struct LIFO *root){
    if(root == NULL){
        printf("Pusta");
        return;
    }
    else if(root->next== NULL) {
        printf("%d ",root->number);
        return;
    }
    else printf("%d ",root->number);
    read(root->next);
}


void delete(struct LIFO **root) {

    if(*root==NULL){
        printf("Pusta");
        return;
    }

    else if((*root)->next == NULL ){
        *root=NULL;
        return;
    }

    struct LIFO* current= (struct LIFO *) *root;

    while(current->next->next!=NULL){
    current=current->next;
    }
    free(current->next);
    current->next=NULL;

}

int main() {

    srand(time(0));

    struct LIFO* lifo = NULL ;

    int userChooser = -1;

    while(userChooser != 0){
        printf("Kolejka Lifo: \n");
        printf("1 - Dodaj element \n");
        printf("2 - Wyswielt wszytskie elementy kolejki \n");
        printf("3 - Usun elemnt kolejki \n");

        scanf("%d", &userChooser);

        if( userChooser == 1){
             prepare(&lifo);
        }
        else if ( userChooser == 2){
            read(lifo);
        }
        else if( userChooser == 3){
            delete(&lifo);
        }
        printf("\n");
    }

    return 0;
}
