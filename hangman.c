#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

char* missing_letters(int,char **);
void create_blanks(char*,int*,int);
void display_film(char*,int);
void display_blank_loc(int*,int);
int cal_blanks(char *);
void blank_displayer(int,int*,char*);
void user_input(char *,char *,int,int*,int);

int lives=10;


int main(){

    srand(time(NULL));
    FILE *fp;

    int count_films=0,i,*blank_locations,count_underscore,len;
    char **films,*movie,*original_movie;

    films=(char **)malloc(sizeof(char *)*1000);
    for(i=0;i<1000;i++)
        *(films+i)=(char *)malloc(sizeof(char)*100);
    
    fp=fopen("movie-list.txt","r");
    if(fp==NULL)
        exit(1);

    while(!feof(fp)){
        if(fgets(films[count_films],99,fp)!=NULL)
            count_films++;
        }

    movie=missing_letters(count_films,films);
    len=strlen(movie);

    original_movie=(char *)malloc(len+1);
    strcpy(original_movie,movie);
    printf("%s\n",original_movie);

    count_underscore=cal_blanks(movie);
    //printf("%d\n",count_underscore);
    blank_locations=(int *)malloc(sizeof(int)*count_underscore);
    if(blank_locations==NULL)
        exit(3);

    create_blanks(movie,blank_locations,count_underscore);
    display_blank_loc(blank_locations,count_underscore);
    blank_displayer(count_underscore,blank_locations,movie);
    display_film(movie,lives);
    user_input(original_movie,movie,lives,blank_locations,count_underscore);

    free(films);
    free(blank_locations);
    fclose(fp);
    return(0);
}

char* missing_letters(int no_of_films,char **movies){
    int choice=(rand()%no_of_films);
    return movies[choice];
}

void display_film(char* film,int lives){
    printf("%s",film);
    printf("  LIVES: %d\n",lives);
}

int cal_blanks(char *movie){
    int underscores,length;
    length=strlen(movie);
    underscores=(rand()%(length))+1;

    return underscores;
}
void display_blank_loc(int* locations,int no_of_underscores){
    int i;
    //printf("\nThe no of underscores are %d\n",no_of_underscores);
    //printf("The blanks are located at\n");
    for(i=0;i<no_of_underscores;i++)
        printf("%d ",locations[i]);
    putchar('\n');
}

void blank_displayer(int underscores,int *blank_locations,char *movie){
    int i=0,length;
    length=strlen(movie);
    for(i=0;i<underscores;i++)
        movie[blank_locations[i]]='_';
}


void create_blanks(char *movie,int* blank_locations,int underscores){
    int locations,length;
    int i,k=0;

    length=strlen(movie);
    blank_locations[0]=((rand())%(length-1));

    for(i=1;i<underscores;i++){
        blank_locations[i]=((rand())%(length-1));
            for(k=0;k<i;k++){
                    while(blank_locations[i]==blank_locations[k]){
                        blank_locations[i]=((rand())%(length-1));
                    }
                }
            }
    }

void user_input(char* original_movie,char *movie,int lives,int* blank_locations,int underscores){
    int i,j,k=0,tries=0,success=0,length;
    char ch;

    length=strlen(original_movie);

    for(i=0;i<lives;i++){
        scanf("%c",&ch);
        fflush(stdin);
        if(islower(ch)!=0)
            ch=toupper(ch);
        for(j=0;j<underscores;j++){
            if(original_movie[blank_locations[j]]==ch){
                movie[blank_locations[j]]=ch;
                success++;
                continue;
               }
            }
            display_film(movie,lives);
            if(success==0){
                printf("Wrong guess!\n");
                lives--;
                display_film(movie,lives);
            }
            tries++;
            success=0;
            if(strcmp(movie,original_movie)==0){
                printf("Correct! Your score is %d\n",tries);
                break;
            }
    }
}









