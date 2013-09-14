/* Copied from the article:
Parallel programming in C and Python
http://dl.acm.org/citation.cfm?id=2240080
*/

#include <stdio.h>
#include <omp.h>

int main (int argc, char **argv) {

  int nthreads, tid, i;

  /* Get the number of processors */

  printf("Number of processors available:: %d\n",omp_get_num_procs());

  /* Set the number of threads to the number of processors */

  omp_set_num_threads(omp_get_num_procs());

  /* Fork a team of threads with each thread having a 

     private tid variable * */

#pragma omp parallel private(tid)

  {

    /* Obtain and print thread id */

    tid = omp_get_thread_num();
    printf("Hello World from thread = %d\n", tid);

    /* Only master thread does this */

    if (tid == 0)

      {

	nthreads = omp_get_num_threads();

	printf("Number of threads = %d\n", nthreads);

      }

  } /* All threads join master thread and terminate */

  return 0;

}
