%{ 
#include <stdio.h> 
#include <stdlib.h> 
%} 
%token ID NUM WHILE DO LE GE EQ NE OR AND 
%right "=" 
%left OR AND 
%left '>' '<' LE GE EQ NE 
%left '+' '-' 
%left '*' '/' 
%right UMINUS 
%left '!' 
%% 
S
         : ST { 
printf("Valid while statement\n");  
exit(0); 
 
 
} 
 
ST       : WHILE '('E')' DEF; 
 
DEF    : '{' BODY '}' 
           | E';' 
           | ST 
           | 
           ; 
 
BODY  : BODY BODY 
           | E ';'        
           | ST 
           |             
           ; 
        
E        : ID '=' E 
          | E '+' E 
          | E '-' E 
          | E '*' E 
          | E '/' E 
          | E '<' E 
          | E '>' E 
          | E LE E 
          | E GE E 
          | E EQ E 
          | E NE E 
          | E OR E 
          | E AND E 
          | E '+' '+' 
          | E '-' '-' 
          | ID  
          | NUM 
          ;  
%% 
 
main() { 
printf("Enter the while statement to check :"); 
    yyparse(); 
     
}    
int yywrap(void) 
{ 
   return 1; 
} 
int yyerror(char *mes) { 
   printf("Invalid statement\n"); 
   return 0; 
}   