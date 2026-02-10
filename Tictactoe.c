#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h> // Sleep 함수 사용을 위해 추가 (컴퓨터 생각하는 척)

char board[3][3] = { {'1','2','3'}, {'4','5','6'}, {'7','8','9'} };

void drawBoard() {
    system("cls || clear");
    printf("\n--- Tic Tac Toe (VS Computer) ---\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", board[i][j]);
            if (j < 2) printf("|");
        }
        if (i < 2) printf("\n---|---|---\n");
    }
    printf("\n");
}

int checkWin() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return 1;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return 1;
    }
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return 1;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return 1;
    return 0;
}

int main() {
    int choice, row, col, moveCount = 0;
    srand((unsigned int)time(NULL));

    while (moveCount < 9) {
        drawBoard();

        // 1. 플레이어 턴 (X)
        printf("번호를 선택하세요 (1-9): ");

        // [수정] 숫자가 아닌 입력이 들어올 경우 무한 루프 방지
        if (scanf("%d", &choice) != 1) {
            printf("숫자만 입력할 수 있습니다!\n");
            while (getchar() != '\n'); // 입력 버퍼 비우기
            Sleep(1000); // 1초 대기 후 다시 그리기
            continue;
        }

        row = (choice - 1) / 3;
        col = (choice - 1) % 3;

        // [보완] 범위 체크 및 중복 체크
        if (choice < 1 || choice > 9 || board[row][col] == 'X' || board[row][col] == 'O') {
            printf("잘못된 위치이거나 이미 선택된 칸입니다.\n");
            while (getchar() != '\n'); // 버퍼 비우기
            Sleep(1000);
            continue;
        }

        board[row][col] = 'X';
        moveCount++;

        if (checkWin()) {
            drawBoard();
            printf("축하합니다! 당신이 이겼습니다!\n");
            return 0;
        }
        if (moveCount == 9) break;

        // 2. 컴퓨터 턴 (O)
        printf("컴퓨터가 생각 중...\n");
        Sleep(800); // 컴퓨터가 고민하는 느낌을 줌

        while (1) {
            int aiChoice = rand() % 9 + 1;
            int r = (aiChoice - 1) / 3;
            int c = (aiChoice - 1) % 3;
            if (board[r][c] != 'X' && board[r][c] != 'O') {
                board[r][c] = 'O';
                break;
            }
        }
        moveCount++;

        if (checkWin()) {
            drawBoard();
            printf("컴퓨터가 이겼습니다! 다시 도전해보세요.\n");
            return 0;
        }
    }

    drawBoard();
    printf("무승부입니다!\n");
    return 0;
}