#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

static const int BUFSIZE = 1024;

int main(void) {
  char buf[BUFSIZE];
  ssize_t nr;

 start:
  fd = open("./read_file.txt",
  nr = read(fd, buf, BUFSIZE);
}
