/* This AES-128 comes from https://github.com/kokke/tiny-AES128-C which is released into public domain */
#include <stdlib.h>
#include <stdint.h>

extern uint8_t shift_rows[16]; // TODO:

void Randomize_permuation(void);
