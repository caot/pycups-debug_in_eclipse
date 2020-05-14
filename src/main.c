/*
 ============================================================================
 Name        : pycups-debug_in_eclipse.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

#include "py_import_call_execute.h"

int main(int argc, const char *argv[]) {

  for (int i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }

  return import_call_execute(argc, argv);
}
