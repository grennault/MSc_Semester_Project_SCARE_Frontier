// Random AES Shift Rows function

/*****************************************************************************/
/* Includes:                                                                 */
/*****************************************************************************/
#include <stdlib.h>
#include <stdint.h>
#include <string.h> // CBC mode, for memset

/*****************************************************************************/
/* Defines:                                                                  */
/*****************************************************************************/
// The number of columns comprising a state in AES. This is a constant in AES. Value=4
#define Nb 4
// The number of 32 bit words in a key.
#define Nk 4
// Key length in bytes [128 bit]
#define KEYLEN 16
// The number of rounds in AES Cipher.
#define Nr 10

/*****************************************************************************/
/* Private variables:                                                        */
/*****************************************************************************/

// The lookup-tables are marked const so they can be placed in read-only storage instead of RAM
// The numbers below can be computed dynamically trading ROM for RAM -
// This can be useful in (embedded) bootloader applications, where ROM is often limited.

uint8_t shift_rows[16] = {
    // 0     1    2      3     4    5     6     7      8    9     A      B    C     D     E     F
    // Normal Shift rows
    0x00, 0x01, 0x02, 0x03, 0x05, 0x06, 0x07, 0x04, 0x0A, 0x0B, 0x08, 0x09, 0x0F, 0x0C, 0x0D, 0x0E};
/*    0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};
 */

void Randomize_permuation(void)
{
  uint8_t i, tmp;
  for (i = 0; i < 15; ++i)
  {
    uint8_t j = ((uint8_t)rand()) >> 4; // A random integer such that i ≤ j < 16
    tmp = shift_rows[i];
    shift_rows[i] = shift_rows[j];
    shift_rows[j] = tmp;
  }
}