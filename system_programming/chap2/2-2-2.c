#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

int main(void) {
  ssize_t ret;
  int fd;
  unsigned long buf;
  size_t len;
  len = sizeof(unsigned long);
  fd = open("./read_file.txt", O_RDONLY);
  while (len != 0 && (ret = read(fd, &buf, len)) != 0) {
    if (ret == -1){
      if(errno == EINTR)
	continue;
      perror("read");
      break;
    }

    len -= ret;
    buf += ret;
  }
  printf("%lu\n",buf);
}
