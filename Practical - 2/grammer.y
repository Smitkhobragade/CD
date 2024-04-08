%{ 
#include<stdio.h> 
#include<stdlib.h> 
%} 
%token A B C

%% 
stmt: S C { printf("It is Valid string of the given format\n"); 
			exit(0); } 
; 
S: A S B 
| A B
	
; 
%% 

int yyerror(char *msg) { 
	printf("Invalid string\n"); 
	exit(0); 
} 

void main() { 
	printf("Enter the string\n"); 
	yyparse(); 
} 
