#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Allocate some memory to the passed arg and zero it out
void do_task(unsigned char **p) {
  *p = (unsigned char *) malloc(8 * sizeof(unsigned char));

  memset(*p, '\0', 8 * sizeof(unsigned char));

  return;

}


int main(void) {

  printf("Doing some pointless task...\n");
  
  unsigned char *p;

  do_task(&p);

  free(p);


  printf("Done doing task. Exiting...\n");
  
  return 0;

}

