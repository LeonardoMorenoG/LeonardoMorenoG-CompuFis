#include<stdlib.h>
#include<stdio.h>

float* loadData(char* file, int *numRows, int *numColumns);

int main(int argc, char** argv){
    
    char* fileInName=argv[1];
    float* data;
    int nRow=0;
    int nColumns=2;

    data=loadData(fileInName, &nRow, &nColumns);
    
    int i=0;    
    for(;i<nRow*nColumns;i++){
      printf("%d, ", data[i]);
    }
    /**float* matrixT;
       matrixT = organizeTimeMatrix(*data, nRow, nColumns);**/
    return 0;
}

float* loadData(char* file, int* numRows, int* numColumns){ 
    FILE* in;
    in = fopen(file, "r");
    if(!in){
      printf("The File can't be readed");
      exit(1);
    }
    //get the number of rows in the file
    int test;
    do{
      test=fgetc(in);
      if(test == '\n'){
	*numRows++;
      }
    }while(test!=EOF);
    rewind(in);

    /**OMITIDO PA PROBAAAR
    char* string;
    while(feof(in)){
      fgets(string,100, in);
      *numRows++;
    }**/


    //get the information of the file and store it
    float *dataStore;
    dataStore = malloc((*numRows * *numColumns)* sizeof(float));
    int i=0;
    for(; i<*numRows * *numColumns; i++){
      fscanf(in, "%d %d\n",dataStore[i], dataStore[i+1] );
    }
    return dataStore;
}

