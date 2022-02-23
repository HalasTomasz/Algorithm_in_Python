#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct FIFO{
    int number;
    struct FIFO* next;
};

void prepare(struct FIFO **root){
    if(*root == NULL){
        *root=(struct FIFO*)malloc(sizeof (struct FIFO*));
        (*root)->number=rand()%5;
        (*root)->next=NULL;
        return;
    }

    struct FIFO *current = *root;
    while(current->next!=NULL){
        current=current->next;
    }
    current->next=(struct FIFO*)malloc(sizeof (struct FIFO*));
    current->next->number=rand()%5;
    current->next->next=NULL;
}


void read(struct FIFO *root){
    if(root==NULL){
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


void delete(struct FIFO **root) {

    if(*root== NULL ){
        printf("Pusta");
        return;
    }
    struct FIFO* current= (*root)->next;
    free(*root);
    *root= (struct FIFO *) current;
}



int main() {

    srand(time(0));

    struct FIFO* pFifo = NULL;

    int userChooser = -1;

    while(userChooser != 0){
        printf("Kolejka FIFO: \n");
        printf("1 - Dodaj element \n");
        printf("2 - Wyswielt wszytskie elementy kolejki \n");
        printf("3 - Usun elemnt kolejki \n");

        scanf("%d", &userChooser);

        if( userChooser == 1){
            prepare(&pFifo);
        }
        else if ( userChooser == 2){
            read(pFifo);
        }
        else if( userChooser == 3){
            delete(&pFifo);
        }
        printf("\n");
    }

    return 0;
}
