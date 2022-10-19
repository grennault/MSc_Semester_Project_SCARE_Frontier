#include <stdio.h>
#include <stdint.h>
#include <string.h> // CBC mode, for memset
#include <stdlib.h>
#include <time.h>

typedef uint8_t state_t[4][4];
static state_t *state;
static state_t *state_copy;

uint8_t shift_rows[16] = {
    // 0     1    2      3     4    5     6     7      8    9     A      B    C     D     E     F
    // Normal Shift rows
    // TODO: Test this implementation
    0x00, 0x01, 0x02, 0x03, 0x05, 0x06, 0x07, 0x04, 0x0A, 0x0B, 0x08, 0x09, 0x0F, 0x0C, 0x0D, 0x0E};
// 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};

void Randomize_permuation(void)
{
    uint8_t i, tmp;
    srand(time(0));
    for (i = 0; i < 15; ++i)
    {
        uint8_t j = ((uint8_t)rand()) >> 4; // A random integer such that i ≤ j < 16
        tmp = (uint8_t)shift_rows[i];
        shift_rows[i] = (uint8_t)shift_rows[j];
        shift_rows[j] = (uint8_t)tmp;
    }

    for (i = 0; i < 15; ++i)
    {
        printf("%d ", shift_rows[i]);
    }
    printf("\n");
}

void ShiftRows(void)
{
    // printf("test\n");
    // fflush(stdout);
    uint8_t temp;

    Randomize_permuation();
    printf("Copy of state\n");

    for (temp = 0; temp < 16; ++temp)
    {
        // TODO: Test and characterize
        (*state_copy)[temp / 4][temp % 4] = (*state)[temp / 4][temp % 4];
    }

    for (temp = 0; temp < 16; ++temp)
    {
        printf("%d: (%d) %d%d <- %d%d\n", temp, shift_rows[temp], temp % 4, temp / 4, shift_rows[temp] % 4, shift_rows[temp] / 4);
        // TODO: Test and characterize
        (*state)[temp / 4][temp % 4] = (*state_copy)[shift_rows[temp] / 4][shift_rows[temp] % 4];
    }
    printf("\n");

    int i, j;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("%d, ", (*state)[i][j]);
        }
        printf("\n");
    }

    free(state_copy);
}

int main(void)
{
    printf("Hello World!\n");
    state = (state_t *)malloc(sizeof(state_t) * 16);
    (*state)[0][3] = (uint8_t)0xFF;
    (*state)[1][3] = (uint8_t)0xFF;
    (*state)[2][3] = (uint8_t)0xFF;
    (*state)[3][3] = (uint8_t)0xFF;
    state_copy = (state_t *)malloc(sizeof(state_t) * 16);

    ShiftRows();
    return 0;
}