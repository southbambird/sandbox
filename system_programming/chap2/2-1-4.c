#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(void){
  int fd;

  char file[] = "./create_file.txt";
  fd = creat(file, 0644);
  if (fd == -1){
    /* error */
    printf("error!!\n");
    exit(-1);
  }
  printf("created file!!\n");
}
    
    
