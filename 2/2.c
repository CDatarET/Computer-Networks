#include <stdio.h>
#include <math.h>

int main() {
    int data_bits;
    printf("Enter number of data bits: ");
    scanf("%d", &data_bits);

    // Calculate required parity bits
    int parity_bits = 1;
    while ((1 << parity_bits) < (data_bits + parity_bits + 1)) {
        parity_bits++;
    }

    int total_bits = data_bits + parity_bits;
    printf("Total bits needed: %d (with %d parity bits)\n\n", total_bits, parity_bits);

    int data[total_bits + 1];
    int datacheck[total_bits + 1];
    int i, j, c, syndrome = 0;

    // Initialize array
    for (i = 0; i <= total_bits; i++) {
        data[i] = 0;
        datacheck[i] = 0;
    }

    // Input data bits (non-parity positions)
    printf("Enter %d data bits one by one (0 or 1):\n", data_bits);
    int bit_index = 0;
    for (i = 1; i <= total_bits && bit_index < data_bits; i++) {
        int is_parity = 0;
        // Check if position i is a power of 2 (parity bit position)
        for (j = 0; j < parity_bits; j++) {
            if (i == (1 << j)) {
                is_parity = 1;
                break;
            }
        }
        if (!is_parity) {
            int bit;
            while (1) {
                printf("Bit %d: ", bit_index + 1);
                if (scanf("%d", &bit) != 1) {
                    // Clear input buffer
                    while (getchar() != '\n');
                    printf("Invalid input! Please enter 0 or 1\n");
                    continue;
                }
                if (bit == 0 || bit == 1) {
                    data[i] = bit;
                    break;
                } else {
                    printf("Invalid input! Please enter 0 or 1\n");
                }
            }
            bit_index++;
        }
    }

    // Calculate parity bits
    for (i = 0; i < parity_bits; i++) {
        int parity_pos = 1 << i;  // 2^i
        int parity = 0;
        for (j = 1; j <= total_bits; j++) {
            if (j & parity_pos) {  // Check if bit i is set in position j
                parity ^= data[j];
            }
        }
        data[parity_pos] = parity;
    }

    printf("\nEncoded data is: ");
    for (i = 1; i <= total_bits; i++)
        printf("%d", data[i]);

    printf("\n\nEnter received %d bits one by one\n", total_bits);
    for (i = 1; i <= total_bits; i++)
        scanf("%d", &datacheck[i]);

    // Calculate syndrome
    syndrome = 0;
    for (i = 0; i < parity_bits; i++) {
        int parity_pos = 1 << i;
        int parity = 0;
        for (j = 1; j <= total_bits; j++) {
            if (j & parity_pos) {
                parity ^= datacheck[j];
            }
        }
        syndrome += parity * parity_pos;
    }

    if (syndrome == 0) {
        printf("\nNo error while transmission of data\n");
    }
    else {
        printf("\nFound error at position %d\n", syndrome);

        printf("Data in  : ");
        for (i = 1; i <= total_bits; i++)
            printf("%d", data[i]);

        printf("\nData out : ");
        for (i = 1; i <= total_bits; i++)
            printf("%d", datacheck[i]);

        printf("\nError pos: ");
        for (i = 1; i <= total_bits; i++) {
            if (i == syndrome)
                printf("^");
            else
                printf(" ");
        }
        printf("\n");

        // Show which bit is wrong
        printf("Wrong bit at position %d: received %d, should be %d\n", 
               syndrome, datacheck[syndrome], data[syndrome]);

        // Correct the error
        datacheck[syndrome] = (datacheck[syndrome] == 0) ? 1 : 0;

        printf("\nCorrected data: ");
        for (i = 1; i <= total_bits; i++)
            printf("%d", datacheck[i]);
        printf("\n");
    }

    return 0;
}