#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

int main(void) {
  int fd;
  unsigned long word;
  ssize_t nr;

  fd = open("./read_file.txt",O_RDONLY);

  nr = read(fd, &word, sizeof (unsigned long));
  if(nr == -1){
    /* error */
    printf("error!");
    exit(-1);
  }
  printf("done!\n");
}
