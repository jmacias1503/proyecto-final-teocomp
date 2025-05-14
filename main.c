#include <stdio.h>
struct Node;
struct OutputTransFunc{
  char outputChar;
  int moveHead;
  struct Node* nextState;
};
struct Node{
  char stateName[5];
  struct OutputTransFunc transFunc;
};
void writeOutput(char* tape, int tapePosition, char outputChar){
	tape[tapePosition] = outputChar;
}
struct OutputTransFunc transFunc(struct Node currentState, char inputTape);
int main(){
  int tapePosition = 0;
  printf("Ingresa la palabra a analizar:");
  struct Node q0;
  return 0;
}
