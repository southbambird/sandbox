#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(void) {
  int fd;
  char file[] = "/Users/runx2/work/sandbox/system_programming/chap2/create_file.txt";
    fd = open (file, O_WRONLY | O_CREAT | O_TRUNC,
	       S_IWUSR | S_IRUSR | S_IWGRP | S_IROTH );
  if (fd == -1){
    /* error */
    printf("error!!\n");
    exit(-1);
  }

  printf("create done!!\n");
}
