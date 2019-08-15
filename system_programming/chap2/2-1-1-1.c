#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


int main(void)
{
  int fd;

  fd = open("/Users/runx2/work/sandbox/system_programming/chap2/madagascar",O_RDONLY);
  if (fd == -1){
    /* error */
    printf("error!!\n");
    //exit(-1);
  }
  
  printf("open done\n");

  int fd2;

  fd2 = open("/Users/runx2/work/sandbox/system_programming/chap2/pearl", O_RDONLY | O_TRUNC);
  if (fd2 == -1){
    printf("error2!!\n");
    //exit(-1)
  }
  printf("open done 2\n");

  sleep(15);

}
