/*
    This file is part of the ChipWhisperer Example Targets
    Copyright (C) 2012-2015 NewAE Technology Inc.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
#ifndef AES_INDEPENDANT_
#define AES_INDEPENDANT_

#include <stdint.h>

#define KEY_LENGTH 16
#define DEFAULT_KEY 0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c

void aes_indep_init(void);
void aes_indep_key(uint8_t * key);
void aes_indep_enc(uint8_t * pt);
void aes_indep_enc_pretrigger(uint8_t * pt);
void aes_indep_enc_posttrigger(uint8_t * pt);
void aes_indep_mask(uint8_t * m, uint8_t len);

#endif
